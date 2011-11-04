# -*- coding: utf-8 -*-

from djangorestframework.renderers import JSONRenderer

class JSONPRenderer(JSONRenderer):
    media_type = 'application/json'

    def render(self, obj=None, media_type=None):
        """
        Given an obj, if callback is presented in GET params, return in JSONP
        ;otherwise, return in JSON
        """
        params = self.view.request.GET.copy()
        json_return = super(JSONPRenderer,self).render(obj,media_type)
        if params.get('callback'):
            callback = params.get('callback')
            self.view.response.headers['Content-Type'] = 'application/javascript'
            return "%s(%s)" % (callback, json_return)
        else:
            return json_return
