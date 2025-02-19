# -*- coding: utf-8 -*-
import reflex as rx

from .context import Context

ctx: Context = Context()
app: any = rx.App()
ctx._app = app
ctx.begin(context=ctx)
