# -*- coding: UTF-8 -*-
SECRET_KEY = "I_LOVE_PYTHON_NMSL"

SESSION_TYPE = "redis"
SESSION_PERMANENT = True
SESSION_USE_SIGNER = True
SESSION_KEY_PREFIX = ''
import redis
SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')
