# Creates a file in /tmp
file { '/tmp/holberton':
  ensure  => 'present',
  path    => '/tmp/holberton',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   =>  'www-data'
}
