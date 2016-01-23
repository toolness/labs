# Proxying

The `proxy` command lets you proxy requests on the remote server to
your machine.

Let's say we've got an `index.html` file in our home directory:

    $ printf "Hi there" > index.html

Now, in one terminal, let's start an HTTP server:

    $ python -m SimpleHTTPServer 8080      # Keep this running.

In another terminal, we'll run our `proxy` command:

    $ labs proxy 8080                      # Keep this running.

Now we'll wait a moment for those to start up and then we'll curl
to our remote server:

    $ sleep 1
    $ curl http://labs:8080/ 2> /dev/null
    Hi there

Note that this functionality does require [`GatewayPorts`][] to
be properly configured on the remote server.

[`GatewayPorts`]: http://askubuntu.com/a/50075
