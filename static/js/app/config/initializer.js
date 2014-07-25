var mainapp = angular.module('mainapp', ['uiSlider','ui.router', 'ui.bootstrap', 'ngResource', 'ngCookies'])
.run(function($rootScope) {
    $rootScope.MEDIA_URL = MEDIA_URL;
})
.config(function($stateProvider, $urlRouterProvider, $interpolateProvider, $httpProvider){
  	$httpProvider.defaults.xsrfCookieName = 'csrftoken';
	$httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
	//$urlRouterProvider.otherwise("/home");
	$stateProvider
	.state('redirect', {
		url: '/_=_',
		views:{
			'viewBody': { templateUrl: "/static/js/app/templates/redirect.html" }
		}
	})
	.state('home', {
        url: "/home",
        views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/home.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
	.state('profile', {
        url: "/profile",
        views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/profile.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
	.state('publicprofile', {
        url: "/profile/:username",
        views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/public_profile.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
    .state('meal', {
    		url: "/meal/:id",
    		views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/meal-details.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
    .state('recipes', {
    		url: "/recipes",
    		views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/recipes.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
    .state('create_meal', {
    		url: '/create',
    		views:{
          	"viewBody": { templateUrl: "/static/js/app/templates/meal-create.html" },
          	"viewFooter": { templateUrl: "/static/js/app/templates/footer.html" }
    		}
    })
    ;
})
.directive('fileInput', ['$parse', function($parse){
	return {
		restrict: 'A',
		link: function(scope, elm, attrs){
			elm.bind('change', function(){
				$parse(attrs.fileInput)
				.assign(scope, elm[0].files);
				scope.$apply();				
			});
		}
	};
}])
.directive('warning', ['$parse', function($parse){
	return {
		restrict: 'E',
		scope: {
			errors: "=errors"
		},
		template: '<label class="control-label" ng-repeat="error in errors" ng-show="errors" ng-class="{\'errors\': \'has-error\'}">{{ error }}</label>'
	};
}])
.directive('formlabel', ['$parse', function($parse){
	return {
		restrict: 'E',
		scope: {
			title: "@"
		},
		template: '<label class="col-md-2 control-label" for="exampleInputPassword1">{{title}}</label>'
	};
}])
.directive('formmidlabel', ['$parse', function($parse){
	return {
		restrict: 'E',
		scope: {
			title: "@"
		},
		template: '<label class="col-md-3 control-label" for="exampleInputPassword1">{{title}}</label>'
	};
}])
;



