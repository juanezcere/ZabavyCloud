# -*- coding: utf-8 -*-
import reflex as rx

from .context import Context

context: Context = Context()
app: any = rx.App()
app.context = context
context.app = app
context.begin(context=context)
