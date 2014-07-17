/*
 * resource example for todos
 */

mainapp.controller('RedirectController', function($location, $cookies){
	var newPath = $cookies.path;
	delete $cookies.path;
	$location.path(newPath); 	
});

mainapp.controller('LoginController', function($scope, Api, $location, $cookies, $http){
	$scope.loggedIn = false;
	Api.UserApi.Login.get().$promise.then(function(data){
		$scope.loggedIn = data.success;
		if(data.success){
			Api.UserApi.UserSelf.query().$promise.then(function(data){
				if(data.length>0){
					$scope.user = data[0];
					Api.UserApi.UserProfileSelf.get().$promise.then(function(profile){
						$scope.user_profile = profile[0];
					});
				}
			});
		}
	});
	$scope.logout = function(){
		Api.UserApi.Logout.get().$promise.then(function(data){
			$scope.loggedIn = false;
		});
		$("#logOutForm").modal("show");
	};
	$scope.loginForm = function(path){
		$cookies.path = path;
		$("#loginForm").modal("show");
	};
	$scope.registerForm = function(path){
		$cookies.path = path;
		$("#registrationForm").modal("show");
	};
	$scope.feedback = function(){
		$("#feedbackForm").modal("show");
	};
	$scope.review = function(){
		$("#reviewModal").modal("show");
	};
	$scope.sendFeedback = function(){
		alert(1);
    	var link = "mailto:info@upcooking.com"
             + "?cc=" + escape(document.getElementById('feedbackEmail').value)
             + "&subject=" + escape(document.getElementById('feedbackTitle').value)
             + "&body=" + escape(document.getElementById('feedbackMessage').value);
		alert(link);
    	window.location.href = link;
	};
	$scope.tryLogin = function(){
		
	};
	$scope.ifLoggedIn = function(path){
		if($scope.loggedIn){
			$location.path(path);
		}
		else{
			$scope.loginForm(path);
		}
	};
	// $scope.isActive = function (path) {
		// var active = (path === $location.path());
		// return active;
	// };
	$scope.goHome = function(){
		$('#logOutForm').modal('hide');
		$timeout(function(){
			window.location = "/#/home";
		}, 500);   
	};
	$scope.login_form_data = {'username': '', 'password': ''};
	$scope.registrationform = {'username': '', 'password1': '', 'password2': ''};
	$scope.login_attempts = 0;
	$scope.regular_register = function(){
		$scope.register_error_message = "";
		$http.post('/register/', $scope.registrationform)
		.success(function(data, status, headers, config){
			if(data.success){
				location.reload();
			}else{
				$scope.register_error_message = data;	
			}
		})
		.error(function(data, status, headers, config){
			$scope.register_error_message = "Something went wrong. Please try again later."
		});
	};
	$scope.regular_login = function(){
		if($scope.login_attempts<=3){
			$scope.login_error_message = "Attempt "+$scope.login_attempts+"/3";
			$http.post('/login/', $scope.login_form_data)
			.success(function(data, status, headers, config){
				if(!data.success){
					$scope.login_attempts = $scope.login_attempts + 1;
					$scope.login_error_message = "You either have the wrong username or password. Please try again later.";
				}
				else{
					location.reload();
				}
			})
			.error(function(data, status, headers, config){
				$scope.login_error_message = "Something went wrong. Please try again later.";
			});
		}
	};
});
