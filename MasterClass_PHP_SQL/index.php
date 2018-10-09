<?php
// Test connexion
$connect = include 'requete.php';
print($connect);



?>

  <!DOCTYPE html>
  <html>

  <head>
    <meta charset="utf-8">
    <link rel="stylesheet" type="text/css" href="index.css">
    <title></title>
  </head>

  <body>
    <form method="get" action="requete.php">
      <label for="student-select">Apprenant:</label>

      <select name='student'  id="student-select">
        <option value="">--Sélectionner un apprenant--</option>
        <?php getList('students');?>
      </select>

    </form>

    <form method="post" action="requete.php">

      <label for="hobby-select">Hobby:</label>

      <select name='hobby' id="hobby-select">
        <option value="">--Sélectionner un hobbby--</option>

        <?php getList('hobbies'); ?>

      </select>

      <br>

      <label for="teacher-select">Formateur:</label>

      <select name='teacher' id="teacher-select">
        <option value="">--Sélectionner un formateur--</option>

        <?php getList('teacher'); ?>

      </select>

      <br>

      <label for="age-select">Age:</label>

      <select name='age' id="age-select">
        <option value="">--Sélectionner un age--</option>

        <?php getList('age'); ?>

      </select>

      <br>

  
      <br> Nom:
      <input type="text" name="lastName" value="">
      <br>
      <br> Prenom:
      <input type="text" name="firstName" value="">
      <br>
      <br> Mail:
      <input type="email" name="email" value="">
      <br>
      <br>

      <input type="submit" name="submit" value="Submit">
    </form>




  </body>

  </html>