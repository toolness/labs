# Git Basics

Let's assume that we're running on a laptop and are (rather unwisely)
doing some coding as the root user.

Let's make a repo!

    $ mkdir /root/my-repo
    $ cd /root/my-repo
    $ git init
    Initialized empty Git repository in /root/my-repo/.git/

And add a file to it...

    $ printf "i am a file" > file.txt
    $ git add file.txt
    $ git commit -m "added file.txt"
    [master (root-commit) ...] added file.txt
    1 file changed, 1 insertion(+)
    create mode 100644 file.txt

Now we'll use our `labs` command to list repos on the remote server.

    $ labs git list

Looks like there's nothing there right now. So we'll add our current repo.

    $ labs git create my-repo
    Initialized empty Git repository in /home/varmaa/git/my-repo/
    Creating remote repository.
    Running 'mkdir git/my-repo && git -C git/my-repo init --bare' on
      varmaa@labs...
    Calling 'git remote add labs varmaa@labs:git/my-repo'...

Now our new repo shows up on the remote server:

    $ labs git list
    my-repo

Note that we haven't actually pushed anything there yet. We can do that
via the git `labs` remote that was set up for us:

    $ git push labs master
    To varmaa@labs:git/my-repo
    * [new branch]      master -> master

We can also remove the machine from our local system:

    $ cd ..
    $ rm -rf my-repo

And then re-clone it from the remote server:

    $ labs git clone my-repo
    Cloning into 'my-repo'...
    Calling 'git clone varmaa@labs:git/my-repo --origin labs'...

We can also delete the remote server's repository too:

    $ labs git destroy my-repo
    Running 'rm -rf git/my-repo' on varmaa@labs...
    $ labs git list
