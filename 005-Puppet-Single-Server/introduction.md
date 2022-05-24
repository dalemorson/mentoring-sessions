# Puppet Introduction

- This lab will introduce the Puppet Agent on a single Windows Server.
- Puppet can be used in a single server or multi-server architecture.

## Introduction to Windows Server Configuration

- Begin with an overview of Windows Server and manual configuration.

## Installing Puppet

- Download the [MSI Installer](https://puppet.com/docs/pe/2017.3/installing/installing_agents.html#install-windows-agents-with-the-msi-package)
- Install the MSI Installer.
- Confirm the installation worked using PowerShell.

```
puppet
puppet config print config
```

## Puppet - Hello World

- Start with a Hello World manifest.
- Create a new file called `hello.pp`.

```
file { 'c:\hello.txt':
  ensure  => file,
  content => "hello, world\n",
}
```

- Execute the `.pp` file

```
puppet apply hello.pp
```

- A new file called `hello.txt` will be created.

## Resources

- The syntax shown above is a resource declaration and the syntax for these is always this:

```
RESOURCE_TYPE { TITLE:
  ATTRIBUTE => VALUE
}
```

- The `RESOURCE_TYPE` is how you tell Puppet the type of resource you’re declaring. 
- You can check all the available resource types:

```
puppet resource --types
```

- The `TITLE` is the name that puppet uses to identify the resource internally. Every resource must have a unique title. With file resources this is typically the full path to the file (which is therefore unique by nature).
- The `attributes` describe how the resource should be configured. These vary by resource (and there are more for file than were shown above). All resources support ensure but the possible values for it vary by resource.

## Puppet Describe

- Puppet has a built-in tool to help you discover all of the different attributes associated with a resource called Describe. For example:

```
puppet describe file
```
- Returns a description of the file resource and a complete list of all the attributes and their associated valid values.

## Additional Examples

### Services

```
service { 'wuauserv':
  ensure => running,
  enable => true,
}
```

### Users and Groups

```
group { 'Avengers':
  ensure => present,
}

user { 'TonyStark':
  ensure => present,
  password => 'password123',
  groups => ['Avengers'],
}
```

### Scheduled Tasks

```
scheduled_task { 'Run Puppet Every 5 Minutes':
  ensure    => present,
  enabled   => true,
  command   => 'C:/Program Files/Puppet Labs/Puppet/bin/puppet.bat',
  arguments => 'apply C:/puppet',
  working_dir => 'C:/Program Files/Puppet Labs/Puppet/bin/',
  trigger   => {
    schedule   => daily,
	start_time => '08:00',
    minutes_interval => 5,
    minutes_duration => 60,
  }
}
```

### Execute a Script
```
exec { 'do-something':
  command => 'C:/something.exe'
}
```