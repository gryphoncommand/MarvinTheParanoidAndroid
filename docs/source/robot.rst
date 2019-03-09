Main Module: *robot.py*
=======================

This file is the nexus of our project. It is interconnected to everything
in the project and serves as our main executable file.

Execution Methods
-----------------

For MacBooks:

  .. code-block:: python

    python3 robot.py [ params ]

For Windows:

  .. code-block:: python

    py3 robot.py [ params ]

Params Options:
  - **deploy**: Deploys the code to any robots that it finds, depending on the settings in `deploy.cfg`.
  - **test**: Runs the unit tests under the `tests` directory.
  - **sim**: Unique to RobotPy, this parameter creates a window of buttons and sliders to test the functionality of the robot on.

---------------------

File Info
----------
.. automodule:: robot
    :members:
    :undoc-members:
    :show-inheritance:

.. _this link: https://wpilib.screenstepslive.com/s/currentCS/m/java/l/599732-what-is-command-based-programming
