from functools import wraps
from flask import abort
from flask_login import current_user
from app.models.Models import Permission


def permission_required(permission):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not current_user.can(permission):
                abort(403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(f):
    return permission_required(Permission.ADMINISTER)(f)



#need to modify

# def limit(requests=100, window=60, by="ip", group=None):
#     if not callable(by):
#         by = { 'ip': lambda: request.headers.remote_addr }[by]
#
#     def decorator(f):
#         @functools.wraps(f)
#         def wrapped(*args, **kwargs):
#             group = group or request.endpoint
#             key = ":".join(["rl", group, by()])
#
#             try:
#                 remaining = requests - int(redis.get(key))
#             except (ValueError, TypeError):
#                 remaining = requests
#                 redis.set(key, 0)
#
#             ttl = redis.ttl(key)
#             if not ttl:
#                 redis.expire(key, window)
#                 ttl = window
#
#             g.view_limits = (requests,remaining-1,time()+ttl)
#
#             if remaining > 0:
#                 redis.incr(key, 1)
#                 return f(*args, **kwargs)
#             else:
#                 return Response("Too Many Requests", 429)
#         return wrapped
#     return decorator

# @api.after_request
# def inject_rate_limit_headers(response):
#     try:
#         requests, remaining, reset = map(int, g.view_limits)
#     except (AttributeError, ValueError):
#         return response
#     else:
#         h = response.headers
#         h.add('X-RateLimit-Remaining', remaining)
#         h.add('X-RateLimit-Limit', requests)
#         h.add('X-RateLimit-Reset', reset)
#         return response


# @api.route('/reports/power/monthly//')
# @limit(requests=1, by='ip')
# @background
# def report_monthly_power(year, month):
#     rdata = generate_power_report(year, month)
#     return rdata

#
# def background(f):
#     @functools.wraps(f)
#     def wrapper(*args, **kwargs):
#         jobid = uuid4().hex
#         key = 'job-{0}'.format(jobid)
#         skey = 'job-{0}-status'.format(jobid)
#         expire_time = 3600
#         redis.set(skey, 202)
#         redis.expire(skey, expire_time)
#
#         @copy_current_request_context
#         def task():
#             try:
#                 data = f(*args, **kwargs)
#             except:
#                 redis.set(skey, 500)
#             else:
#                 redis.set(skey, 200)
#                 redis.set(key, data)
#                 redis.expire(key, expire_time)
#             redis.expire(skey, expire_time)
#
#         gevent.spawn(task)
#         return jsonify({"job": jobid})
#     return wrapper