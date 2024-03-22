# Puppet manifest to kill a process

exec { 'killmenow':
command  => 'kill -9 killmenow',
provider => 'shell'
onlyif   => 'ps -ef |grep killmenow'
}
