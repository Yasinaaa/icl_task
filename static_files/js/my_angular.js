/**
 * Created by yasina on 23.04.16.
 */
app = angular.module('test_angular',[]);

angular.module('test_angular', [])
 .controller('DemoCtrl', ['$scope','$http', function($scope,$http) {
   $scope.projects = [];


        $scope.label_click = function(){
             $http.get('/static_fiels/media/all_graphs.json').success(function(data) {
            //$scope.projects = data;
            console.log($scope.projects);
                 $scope.projects = [];

                for(var i=0; i < data.length; i++){
                    console.log(data[i]);
                    $scope.projects.push(data[i])
                }
                $scope.data = {
                    availableOptions: $scope.projects,
                    selectedOption: $scope.projects[0]
                    };
                });
        }

        $scope.label_click();


}]);




