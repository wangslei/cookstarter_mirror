mainapp.controller('UserPublicProfileController', function($scope, $stateParams, Api, $http){
	$scope.user_profile = {};
	Api.UserApi.UserProfile.query({id: $stateParams.username})
	.$promise
	.then(function(data){
	    $scope.user_profile = data;
	});
});
