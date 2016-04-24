/**
 * Created by yasina on 23.04.16.
 */
app = angular.module('test_angular',[]);

/*app.controller('DemoCtrl',['$scope', function($scope){
    $scope.model = { id: 2 };
  })*/
angular.module('test_angular', [])
 .controller('DemoCtrl', ['$scope','$http', function($scope,$http) {
   $scope.projects = [];

        // /home/yasina/PycharmProjects/icl_task/static_files/

    $http.get('/media/all_graphs.json').success(function(data) {
    //$scope.projects = data;
    console.log($scope.projects);

        for(var i=0; i < data.length; i++){
            console.log(data[i]);
            $scope.projects.push(data[i])
        }
        $scope.data = {
    availableOptions: $scope.projects,
    selectedOption: {"id": 1, "title": "m"} //This sets the default value of the select in the ui
    };
});
   /*$scope.data = {
    availableOptions: [
      {id: '1', name: 'Option A'},
      {id: '2', name: 'Option B'},
      {id: '3', name: 'Option C'}
    ],
    selectedOption: {id: '3', name: 'Option C'} //This sets the default value of the select in the ui
    };*/


}]);

  /*  $scope.save = function(){
        //$scope.str = document.getElementsByTagName("a")[0].textContent;
        $scope.str = document.getElementById("like").getAttribute('value');
        //$(".data").html("Click=" + document.getElementById("like").getAttribute('value'));

        $(".data").html("Click=" + $scope.str);


        //i = "/home/yasina/PycharmProjects/icl_task/media/graphs/8j.png";

        var div2=$('.foo');
        var elem = document.createElement("img");

        //elem.setAttribute("src", "media/graphs/");
        elem.setAttribute("height", "768");
        elem.setAttribute("width", "1024");
        document.getElementById("foo").appendChild(elem);
        elem.src = 'static_fiels/media/graphs/' + $scope.str + '.png'
         //elem.src = "{% static \'media/graphs/jj.png\' %}"
        //div2.attr('src', "/media/graphs/8j.png");
    }
}]);*/



