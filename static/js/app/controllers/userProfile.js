mainapp.controller('UserProfileController', function($scope, $stateParams, Api, $http){
	$scope.user_profile = {};
	$scope.old_user_profile = {};
	$scope.profileFormErrors = {};
	$scope.profileImageForm = {};
	$scope.profileImageFormErrors = {};
	$scope.userloggedin = false;

	Api.UserApi.UserSelf.query().$promise.then(function(data){
		if(data.length>0){
			$scope.user_id = data[0].id;
			Api.UserApi.UserProfileSelf.get().$promise.then(function(data){
				$scope.user_profile = data[0];
			});
			$scope.userloggedin = true;
		}
	});

	$scope.submitPictureForm = function(){
		if(!$scope.userloggedin){
			alert("PLEASE SIGN IN TO CREATE A RECIPE!!!");	//user not signed in, redirect to sign in page
		}
		else{
			var form = new FormData();
			for(var key in $scope.profileImageForm){
				if(key=="docfile"){
					for(var keyForFile in $scope.profileImageForm[key]){
						form.append("docfile", $scope.profileImageForm[key][keyForFile]);
					}
				}
				else
				{
					form.append(key, $scope.profileImageForm[key]);
				}
			}
			//do some http post or form submit. 
			$http.post(
				'/profile/'+$scope.user_id+'/',
				form,
				{
					transformRequest: angular.identity,
					headers: {'Content-Type': undefined}
				}
			).success(function(newrecipe){
				Api.UserApi.UserProfileSelf.get().$promise.then(function(data){
					$scope.user_profile = data[0];
					$('#editprofilepicture').modal('hide');
				});
			}).error(function(data){
				$scope.profileImageFormErrors = data;
			});
			//headers: {'Content-Type': 'multipart/form-data'},
		}
	};
	$scope.changePictureModal = function(){
		$('#editprofilepicture').modal('show');	
	};
	$scope.editProfile = function(){
		$scope.old_user_profile = {};
		angular.copy($scope.user_profile, $scope.old_user_profile); 
		$('#editprofile').modal('show');	
	};
	$scope.updateProfile = function(){
		delete $scope.user_profile["docfile"];
		$scope.user_profile.$update(function(data){
			$scope.profileFormErrors = {};
			$('#editprofile').modal('hide');
		}, function(error){
			angular.copy($scope.old_user_profile, $scope.user_profile);
			$scope.profileFormErrors = error.data;
		});
	};
	$scope.activeMealsFilter = function(hosted_meal){
		//this function needs to return true when hosted_meal's start_time is in the future (>new Date())
		return true;
	};
});
