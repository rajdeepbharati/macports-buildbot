# macports-buildbot

## Setting up buildbot 2.x master and worker for testing on localhost

### Setting up buildbot master on localhost

#### 1. Create virtualenv and install buildbot

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

#### 2. Create new directory with buildbot master configuration

    mkdir mp-buildbot && cd mp-buildbot
    buildbot create-master master

#### 3. Add and edit sample configuration files

    cd master
    ln -s .../path/to/contrib/buildbot-test/master.cfg
    cp .../path/to/contrib/buildbot-test/config.sample.yml config.yml
    cp .../path/to/contrib/buildbot-test/workers.sample.yml workers.yml
    cp .../path/to/contrib/buildbot-test/secrets.sample.yml secrets.yml

Check settings in `config.yml` and adapt as needed.

#### 4. Set up authentication

    cd mp-buildbot/master
    htpasswd -c -d ./htpasswd admin

#### 5. Starting buildbot

To start buildbot, execute the `start` command. The OS X firewall will
request you to allow access for Python. Then you can view the buildbot
instance in your web browser.

    buildbot start mp-buildbot/master
    open http://localhost:8010/

#### 5. Testing changes

After making any changes to `master.cfg`, you can reload the
configuration with the `reconfig` command. This is faster than doing
a full `restart`. In a similar way, you can completely `stop` the
buildbot.

    buildbot reconfig mp-buildbot/master

    buildbot restart mp-buildbot/master

    buildbot stop mp-buildbot/master

### Setting up buildbot worker on localhost

#### 1. Create workers

    cd mp-buildbot

    buildbot-worker create-worker worker-base localhost:9989 base_10_14_x86_64 pwd
    buildbot-worker create-worker worker-ports localhost:9989 ports_10_14_x86_64 pwd

#### 2. Install tools

Make sure `getopt` is installed in `/opt/macports-test` prefix of MacPorts installation.

#### 3. Set PATH

    export PATH=$PATH:/opt/local/bin:/opt/local/sbin:/bin:/usr/bin:/usr/local/bin

#### 3. Start the workers

    sudo buildbot-worker start worker-base
    sudo buildbot-worker start worker-ports
