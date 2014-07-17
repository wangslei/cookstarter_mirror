mainapp.controller('HostedMealDetailsController', function($scope, $stateParams, Api, $location, $cookies){
	$scope.today = new Date();
	$scope.meal = {};
	var reloadMeal = function(){
		Api.UserApi.HostedMeal.get({id: $stateParams.id}).$promise.then(function(data){
			$scope.meal = data;
			var arrayDate = $scope.meal.local_start_time.split('T');
			var dateSplit = arrayDate[0].split('-');  
			var timeSplit = arrayDate[0].split(':');  
			var when = new Date(dateSplit[0], parseInt(dateSplit[1])-1, parseInt(dateSplit[2]), 0, 0, 0);
			var dateDiff = when.getTime() - $scope.today.getTime();
			$scope.notoktojoin = $scope.meal.meal_purchases_total>=$scope.meal.maximum_diners_allowed;
			$scope.ableToRequest = new Array();
			for(var i=1;i<=$scope.meal.maximum_diners_allowed-$scope.meal.meal_purchases_total;i++){
				$scope.ableToRequest.push(i);
			}
			Api.UserApi.UserSelf.query().$promise.then(function(data){
				if(data[0]===undefined){}
				else
				{
					$scope.user = data[0].id;
					$scope.userObj = data;
					var alreadyBought = false;
					for(var i=0;i<$scope.meal.meal_purchases_detail.length;i++){
						if($scope.meal.meal_purchases_detail[i].user == $scope.user)
							alreadyBought = true;
					}
					$scope.notoktojoin = $scope.notoktojoin || alreadyBought;
					
				}
			});
		});
	};
	reloadMeal();
	$scope.joinMeal = function(){
		if($scope.user === undefined){
			$cookies.path = 'meal/'+$stateParams.id;
			$("#loginForm").modal("show");
		}else{
			var newpurchaseplan = new Api.UserApi.MealPurchase({
				'purchaser': $scope.user, 
				'quantity': $scope.numGuestsRequest
			});
			newpurchaseplan.$save(function(data){
				$scope.meal.meal_purchases.push(data.id);
				$scope.meal.$update(function(data){
					$("#joinmealcomplete").modal("show");
					reloadMeal();
				}, function(response){
					alert('The connection is not working right now.');
				});
			}, function(response){
					alert('The connection is not working right now.');
			});

		}
	};
});
