<?php  
 
function connect() {
    $connect = pg_connect("host=localhost port=5432 dbname=masterclassdjango user=admin password=admin");
    return $connect;
}

//Try Catch to test connexion
try {
    connect();
    echo 'Connexion réussie';

} catch (Exception $e) {
    echo 'Exception reçue : ',  $e->getMessage(), "\n";
}

//Simple function to get one query
// function getHobbies(){
//     $bdConnect = connect();
//     $queryHobbies = pg_query($bdConnect, "select type_hobbies from masterclass_api_hobbies");
//     $fetchHobbies = pg_fetch_all($queryHobbies);

//     return $fetchHobbies;
// }

function getList($arg){

    $bdConnect = connect();

    switch($arg){
        case 'students':
            $queryStudents = pg_query($bdConnect, "select nom, prenom from masterclass_api_apprenants");
            $fetchStudents = pg_fetch_all($queryStudents);
        
            foreach ($fetchStudents as $student) {
                echo "<option value='".$student['nom']." ".$student['prenom']."'>".$student['nom']." ".$student['prenom']."</option>";
              }

        break;

        case 'hobbies':
            $queryHobbies = pg_query($bdConnect, "select type_hobbies from masterclass_api_hobbies");
            $fetchHobbies = pg_fetch_all($queryHobbies);

            foreach ($fetchHobbies as $hobby) {
                echo "<option value='".$hobby['type_hobbies']."'>".$hobby['type_hobbies']."</option>";
              }

        break;

        case 'teacher':
        $queryTeacher = pg_query($bdConnect, "select nom, prenom from masterclass_api_formateurs");
        $fetchTeacher = pg_fetch_all($queryTeacher);

        foreach ($fetchTeacher as $teacher) {
            echo "<option value='".$teacher['nom']." ".$teacher['prenom']."'>".$teacher['nom']." ".$teacher['prenom']."</option>";
          }
            
        break;

        case 'age':

        echo "<option value='3'>3</option>";

        default:
        echo "No entry!";              
    }
}

echo $_POST['age'];
echo $_POST['teacher'];
echo $_POST['hobby'];
echo $_POST['lastName'];
echo $_POST['firstName'];



    function setNewStudent(){
        $bdConnect = connect();
        $query = pg_query($bdConnect, "INSERT INTO masterclass_api_apprenants (nom,prenom) VALUES (".$_POST['firstName'].", ".$_POST['firstName'].")");
    }




?>
