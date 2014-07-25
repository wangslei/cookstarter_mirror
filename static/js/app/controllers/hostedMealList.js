mainapp.controller('HostedMealController', function($scope, Api){
	$scope.getSlides = function(meal) {
		var slides = [];
		slides.push({
			mealnum: meal.id,
			image: $scope.MEDIA_URL+meal.recipe_detail.docfile,
			text: ""
		});
		if(meal.recipe_detail.docfile2!="recipes/no-img.jpg"){
			slides.push({
				mealnum: meal.id,
				image: $scope.MEDIA_URL+meal.recipe_detail.docfile2,
				text: ""
			});
		}
		if(meal.recipe_detail.docfile3!="recipes/no-img.jpg"){
			slides.push({
				mealnum: meal.id,
				image: $scope.MEDIA_URL+meal.recipe_detail.docfile3,
				text: ""
			});
		}
		if(meal.recipe_detail.docfile4!="recipes/no-img.jpg"){
			slides.push({
				mealnum: meal.id,
				image: $scope.MEDIA_URL+meal.recipe_detail.docfile4,
				text: ""
			});
		}
		if(meal.recipe_detail.docfile5!="recipes/no-img.jpg"){
			slides.push({
				mealnum: meal.id,
				image: $scope.MEDIA_URL+meal.recipe_detail.docfile5,
				text: ""
			});
		}
		return slides;
	};

	function pad(n, width, z) {
  		z = z || '0';
  		n = n + '';
  		return n.length >= width ? n : new Array(width - n.length + 1).join(z) + n;
  	}
	var daysDiff = function(a,b){
		var timeDiff = stripTime(a).getTime() - stripTime(b).getTime();
		var diffDays = Math.ceil(timeDiff / (1000 * 3600 * 24));
		return diffDays;
	};
	function getFutureDate(days){
		return {'date': new Date(+new Date + (864e5 * (days + 1))), 'meals': new Array()};
	}
	function daysSinceSunday(){
		var returnDate = new Date();
		var todayAsDay = returnDate.getDay();
		return -todayAsDay; 
	}
	function stripTime(dateOf){
		var myDate = dateOf;
		var dateWithoutTime = new Date(myDate.getFullYear(), myDate.getMonth(), myDate.getDate());
		return dateWithoutTime;
	}
	var defaultSearchValue = false;
	$scope.search = {
		'recipe_detail': {'is_vegetarian': defaultSearchValue},
		'recipe_detail': {'is_vegan': defaultSearchValue},
		'recipe_detail': {'is_gluten_free': defaultSearchValue},
		'recipe_detail': {'is_dairy_free': defaultSearchValue},
		'recipe_detail': {'is_nut_free': defaultSearchValue},
		'is_pickup': true,
		'is_sitdown': true,
		'min_price_per_serving': '0.00',
		'max_price_per_serving': '100.00',
		'num_search_days': 28,
		'num_search_miles': 5
	};
	
	$scope.days = new Array();
	$scope.firstweek = new Array();
	$scope.min_search_date = new Date();
	$scope.max_search_date = new Date();

	var daysSinceSunday = daysSinceSunday();
	var firstSunday = new Date();
	for(var d=0;d<31;d++){
		var futureDate = getFutureDate(daysSinceSunday+d);
		//alert("today+"+d+"="+JSON.stringify(futureDate));
		$scope.days.push(futureDate);
	}
	$scope.meals = new Array();
	Api.UserApi.HostedMeal.query().$promise.then(function(data){
		var today = new Date();
		angular.forEach(data, function(hostedHeal){
			partyDate = new Date(hostedHeal.local_start_time);
			var diffDaysInt = daysDiff(partyDate, today);
			//alert(hostedHeal.local_start_time+" is "+diffDaysInt);
			if(diffDaysInt<$scope.days.length){
				hostedHeal['slides'] = $scope.getSlides(hostedHeal);
			}
			if(diffDaysInt>=0 && diffDaysInt<$scope.days.length){
				$scope.days[diffDaysInt].meals.push(hostedHeal);
			}
		});
		$scope.meals = data;
	});
	$scope.fullFilter = function(meal){
		var keys = ['is_vegetarian','is_vegan','is_gluten_free','is_dairy_free','is_nut_free'];
		for(var lcv=0;lcv<keys.length;lcv++){
			console.log(meal.recipe_detail);
			if($scope.search.recipe_detail[keys[lcv]] && !meal.recipe_detail[keys[lcv]]){
				return false;
			}
		}
		var sitDownAndPickup = $scope.search.is_pickup && $scope.search.is_sitdown;
		var notSitDownAndPickup = !$scope.search.is_pickup && !$scope.search.is_sitdown;
		if(notSitDownAndPickup){
			return false;
		}
		if(!sitDownAndPickup){
			if($scope.search.is_pickup && !meal.is_pickup){
				return false;
			}
			if($scope.search.is_sitdown && !meal.is_sitdown){
				return false;
			}
		}
		var min_price_per_serving = parseFloat($scope.search.min_price_per_serving);
		if(!isNaN(min_price_per_serving) && min_price_per_serving>meal.price_per_serving){
			return false;
		}
		var max_price_per_serving = parseFloat($scope.search.max_price_per_serving);
		if(!isNaN(max_price_per_serving) && max_price_per_serving<meal.price_per_serving){
			return false;
		}
		var num_search_days = parseInt($scope.search.num_search_days);
		var daysApart = daysDiff(new Date(),new Date(meal.local_start_time));
		if(!isNaN(num_search_days) && num_search_days < daysApart){
			return false;
		}	
		// var max_price_per_serving = parseFloat($scope.search.max_price_per_serving);
		// if(!isNaN(max_price_per_serving) && max_price_per_serving<meal.price_per_serving){
			// return false;
		// }	
		return true;	
	};
});
