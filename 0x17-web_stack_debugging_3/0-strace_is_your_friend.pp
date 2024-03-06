# Web stack debugging 03

$file_path = '/var/www/html/wp-settings.php'

exec { 'Correct php file extension':
  command  => "sed -i 's/.phpp/.php/g' ${file_path}",
  provider => shell,
}
