/*
 * todo api resource example
 */
mainapp.factory('Api', ['$resource', function($resource) {
	var apiRoot = '/api/v1/';
	var api = function(url) {return apiRoot + url;};
	var getJson = function(){return {};};
	var getArray = function(){
		return {
			'get': {method: 'GET', params: {}, isArray: true},
			'save': {method: 'POST', params: {}},
			'delete': {method: 'DELETE', params: {id: "@id"}},
			'update': {method: 'PUT', params: {id: "@id"}}
		};
	};
	return {
		'UserApi': {
			'Login': $resource('/login/#', getJson(), {
					'get': {method: 'GET', params: {}, isArray: false},
					'login': {method: 'POST', params: {}, isArray: false}
				}),
			'Logout': $resource('/logout/#', getJson(), {
					'get': {method: 'GET', params: {}, isArray: false}
				}),
            'UserSelf': $resource(api('user_self/:id/#')),
            'UserProfileSelf': $resource(api('userprofile_self/:id#'), {id:'@id'},
                    {
                        'query': {method: 'GET', params: {}, isArray: false},
                        'get': {method: 'GET', params: {}, isArray: true},
                        'save': {method: 'POST', params: {}},
                        'delete': {method: 'DELETE', params: {id: "@id"}},
                        'update': {method: 'PUT', params: {id: "@id"}}
                    }
            ),
			'User': $resource(api('user/:id#')),
			'UserProfile': $resource(api('UserProfile/:id/#'), {id:'@id'},
					{
                        'query': {method: 'GET', params: {}, isArray: false},
						'get': {method: 'GET', params: {}, isArray: true},
						'save': {method: 'POST', params: {}},
						'delete': {method: 'DELETE', params: {id: "@id"}},
						'update': {method: 'PUT', params: {id: "@id"}}
					}
			),
			'HostedMeal': $resource(api('HostedMeal/:id/#'), {id:'@id'},
					{
						'get': {method: 'GET', params: {}, isArray: false},
						'save': {method: 'POST', params: {}},
						'delete': {method: 'DELETE', params: {id: "@id"}},
						'update': {method: 'PUT', params: {id: "@id"}}
					}
				),
			'Recipe': $resource(api('Recipe/:id#'), {},
					{
						'get': {method: 'GET', params: {}, isArray: true},
						'save': {method: 'POST', params: {}},
						'delete': {method: 'DELETE', params: {id: "@id"}},
						'update': {method: 'PUT', params: {id: "@id"}}
					}
			),
			'MealPurchase': $resource(api('MealPurchase/:id#'), {},
					{
						'get': {method: 'GET', params: {}, isArray: true},
						'save': {method: 'POST', params: {}},
						'delete': {method: 'DELETE', params: {id: "@id"}},
						'update': {method: 'PUT', params: {id: "@id"}}
					}
				) 				 
			}
		};
}]);

