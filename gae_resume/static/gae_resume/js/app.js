// Registering the AngularJS modules
var app = angular.module('app', ['angular-kudos']);

// Angular Controller for Main Page
app.controller('MainCtrl', function($scope, $http) {
    $scope.addCount = function(){

        //Send the AJAX request
        var request = $http({
            method: "post",
            url: "/kudos",
            data: {
                count: 1
            }
        });
        
        // Update the kudos count on the html page.
        request.success(
            function( html ) {
                $('#kudu_count').html(html.count);
            }
        );
    };
});
