#!/usr/bin/env python3

import os
from aws_cdk import core

from stack.events_stack import EventsStack


app = core.App()
EventsStack(app, "python-events-stack")


app.synth()
