# macports-buildbot

## Setting up buildbot 2.x master and worker for testing on localhost

### Setting up buildbot master on localhost

#### 1. Create virtualenv and install buildbot

    python3 -m venv .venv
    source .venv/bin/activate
    pip install buildbot buildbot-worker

#### 2. Create new directory with buildbot master configuration

    mkdir mp-buildbot && cd mp-buildbot
    buildbot create-master master

#### 3. Add and edit sample configuration files

    cd master
    ln -s .../path/to/contrib/buildbot-test/master.cfg
    cp .../path/to/contrib/buildbot-test/config.json.sample config.json
    cp .../path/to/contrib/buildbot-test/slaves.json.sample slaves.json

Check settings in `config.json` and adapt as needed.

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
