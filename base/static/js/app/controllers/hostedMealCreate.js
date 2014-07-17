mainapp.controller('HostedMealCreateController', function($scope, $stateParams, Api, $http, $timeout){
	$scope.customSort = function(recipe){
		var isCreator = recipe.creator==$scope.user_id;
		var creatorBit = isCreator ? '1':'0';
		var str = creatorBit 
		var pad = "0000"
		return pad.substring(0, pad.length - str.length) + recipe.name;
	};
	$scope.goHome = function(){
		$('#hostedmealcompletemodal').modal('hide');
		$timeout(function(){
			window.location = "/#/home";
		}, 1500);     
	};
	$scope.numberToShow = 10;
	$scope.recipes = new Array();
	$scope.recipeAdded = false;
	$scope.recipeFormData = {};
	$scope.recipeFormErrors = {};
	$scope.recipeSelected = false;
	$scope.hostFormData = {
		"price_per_serving": 1,
		"minimum_diners_required": 8,
		"maximum_diners_allowed": 12,
		"is_sitdown": false,
		"is_pickup": false
	};
	$scope.hostFormErrors = {};
	$scope.userloggedin = false;
	$scope.dateOptions = {
		'year-format': "'yy'",
		'starting-day': 1
 	};
 	
 	//timepicker stuff
	$scope.pickertime = new Date();

	$scope.hstep = 1;
	$scope.mstep = 15;

	$scope.options = {
		hstep: [1, 2, 3],
		mstep: [1, 5, 10, 15, 25, 30]
	};

	$scope.ismeridian = true;
	$scope.toggleMode = function() {
		$scope.ismeridian = ! $scope.ismeridian;
	};

	$scope.update = function() {
		var d = new Date();
		d.setHours( 19 );
		d.setMinutes( 30 );
		$scope.pickertime = d;
	};

	$scope.changed = function () {
		console.log('Time changed to: ' + $scope.pickertime);
	};

	$scope.clear = function() {
		$scope.pickertime = null;
	};
	//end timepicker stuff
 	
 	$scope.open = function($event) {
	    $event.preventDefault();
	    $event.stopPropagation();
    	$scope.opened = true;
  	};
  	
	Api.UserApi.UserSelf.query().$promise.then(function(data){
		if(data.length>0){
			$scope.recipeFormData["creator"] = data[0].id; 
			$scope.hostFormData["host"] = data[0].id;
			$scope.userloggedin = true;
			$scope.user_id = data[0].id;
			Api.UserApi.UserProfileSelf.get().$promise.then(function(data){
				$scope.user_profile = data[0];
				$scope.hostFormData.contact_phone = $scope.user_profile.contact_phone;
				$scope.hostFormData.location = $scope.user_profile.location;
			});
			Api.UserApi.Recipe.query({'creator': $scope.user_id}).$promise.then(function(data){
				$scope.recipes = data;
			});
		}
		else{
			//alert("Please log in to save your recipe.")
			$('#loginmodal').modal('show');
		}
	});
	// $scope.init = function() {
		// $scope.hostFormData.contact_phone = $scope.user_profile.contact_phone;
	// };
	$scope.showing = 1;
	$scope.filesChanged = function(elm){
		$scope.recipeFormData.docfile = elm.files;
		$scope.$apply();
	};
	$scope.editRecipe = function(recipeSelected){
		$scope.recipeEdit=true;
		$scope.recipeFormErrors={};
		$scope.recipeFormData=recipeSelected;
	};
	$scope.cloneRecipe = function(recipeSelected){
		$http.post(
			'/recipe/clone/'+$scope.recipeSelected.id+'/'
		).success(function(newrecipe){
			$scope.selectCreateRecipe = "select";
			$("#completedRecipe").modal("show");
			Api.UserApi.Recipe.query().$promise.then(function(data){
				$scope.recipes = data;
				$scope.recipeFormErrors = {};
				$scope.recipeSelected.creator_read_only.id = $scope.user_id; // so that every recipe created is associated with this user
				for(var i=0;i<data.length;i++){
					if(data[i].name == $scope.recipeFormData.name){
						$scope.recipeSelected = $scope.recipes[i];
					}
				}
				$scope.recipeFormData = {};
			});
		});
	};
	$scope.createRecipe = function(isEdit){
		if(!$scope.userloggedin){
			var warn_word = isEdit ? 'EDIT':'CREATE';
			alert("PLEASE SIGN IN TO " + warn_word + " A RECIPE!!!");	//user not signed in, redirect to sign in page	
		}
		else{
			var form = new FormData();
			for(var key in $scope.recipeFormData){
				if(key.indexOf("docfile")==0){
					for(var keyForFile in $scope.recipeFormData[key]){
						form.append(key, $scope.recipeFormData[key][keyForFile]);
					}
				}
				else
				{
					form.append(key, $scope.recipeFormData[key]);
				}
			}
			//do some http post or form submit. 
			if(isEdit){
				$http.post(
					'/recipe/edit/'+$scope.recipeSelected.id+'/',
					form,
					{
						transformRequest: angular.identity,
						headers: {'Content-Type': undefined}
					}
				).success(function(newrecipe){
					$scope.selectCreateRecipe = "select";
					$("#completedRecipe").modal("show");
					Api.UserApi.Recipe.query().$promise.then(function(data){
						$scope.recipes = data;
						$scope.recipeFormErrors = {};
						$scope.recipeSelected.creator_read_only.id = $scope.user_id; // so that every recipe created is associated with this user
						for(var i=0;i<data.length;i++){
							if(data[i].name == $scope.recipeFormData.name){
								$scope.recipeSelected = $scope.recipes[i];
							}
						}
						$scope.recipeFormData = {};
					});
				}).error(function(data){
					$scope.recipeFormErrors = data;
				});
				//headers: {'Content-Type': 'multipart/form-data'},
			}
			else{
				$http.post(
					'/recipe/create/',
					form,
					{
						transformRequest: angular.identity,
						headers: {'Content-Type': undefined}
					}
				).success(function(newrecipe){
					$scope.selectCreateRecipe = "select";
					$("#completedRecipe").modal("show");
					Api.UserApi.Recipe.query().$promise.then(function(data){
						$scope.recipes = data;
						$scope.recipeFormErrors = {};
						$scope.recipeSelected.creator_read_only.id = $scope.user_id; // so that every recipe created is associated with this user
						for(var i=0;i<data.length;i++){
							if(data[i].name == $scope.recipeFormData.name){
								$scope.recipeSelected = $scope.recipes[i];
							}
						}
						$scope.recipeFormData = {};
					});
				}).error(function(data){
					$scope.recipeFormErrors = data;
				});
				//headers: {'Content-Type': 'multipart/form-data'},
			}
		}
	};
	$scope.setRecipe = function(recipe){
		$scope.recipeSelected = recipe;
		$scope.recipeEdit = false;
	};
	$scope.popuplogin = function(url){
		alert("in popuplogin");
		newwindow=window.open(url);
	};
	$scope.activateSlide = function(recipe){
		recipe.active=true;
	};
	$scope.selectRecipeFromCarousel = function(item){
		for(var lcvRecipe=0;lcvRecipe<$scope.recipes.length;lcvRecipe++){
			if($scope.recipes[lcvRecipe].id == item.recipe.id){
				$scope.recipes[lcvRecipe].active = true;
				$scope.hostFormData.recipe = $scope.recipes[lcvRecipe];
				$scope.hostFormData.user = $scope.user_id;
			}
		}
		//console.log(item);	
	};
	$scope.carouselPrev = function(){
		alert("changeSelect");
	};
	$scope.createHost = function(){
		var hostFormData = angular.copy($scope.hostFormData);
		try{
			hostFormData["recipe"] = $scope.hostFormData.recipe.id;
		}catch(err){}
		try{
			hostFormData["start_time"].setHours($scope.pickertime.getHours(),$scope.pickertime.getMinutes(),$scope.pickertime.getSeconds());
		}catch(err){}
		
		var host = new Api.UserApi.HostedMeal(hostFormData);
		host.$save(function(data){
			$scope.hostFormErrors = {};
			$('#hostedmealcompletemodal').modal('show');
		}, function(error){
			$scope.hostFormErrors = error.data;
		});
	};
});