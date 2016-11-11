Build Restore
=============

Build Restore is a Kodi add-on that restores a list of add-ons from their online sources. This add-on facilitates the distribution of Kodi builds as only a list of add-ons and their respective repositories have to be distributed.

Installation
------------

Install Build Restore by going to the Kodi add-ons settings, select "Install from zip file", and select the zip file at ``https://github.com/Flavien/script.buildrestore/archive/master.zip``.

Instructions
------------

Before using the script, you must create a ``build.xml`` file. The ``build.xml`` file must be placed at the root of your ``userdata`` folder (``%APPDATA%\kodi\userdata`` on Windows, ``~/.kodi/userdata/`` on Linux).

The structure of the ``build.xml`` file is the following:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addons>
  <addon id="[addon_1]" />
  <addon id="[addon_2]" />
  ...
</addons>
```

For example:

```
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<addons>
  <addon id="metadata.universal" />
  <addon id="plugin.video.youtube" />
  <addon id="service.subtitles.opensubtitles" />
  <addon id="weather.yahoo" />
  <addon id="skin.eminence.2" />
</addons>
```

The add-on repositories from which the add-ons should be fetched must be installed and enabled for the restore process to work.

Once the ``build.xml`` file has been created, simply execute the Build Restore program to launch the restore process.

License
-------

Copyright 2016 Flavien Charlon

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.