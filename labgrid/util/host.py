import attr


@attr.s(eq=False)
class Host:
    host = attr.ib(validator=attr.validators.instance_of(str))
    sshpassword = attr.ib(
        default=None, validator=attr.validators.optional(attr.validators.instance_of(str)), kw_only=True
    )
    jumps = attr.ib(default=None, validator=attr.validators.optional(attr.validators.instance_of(list)), kw_only=True)
