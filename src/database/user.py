from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    uid = fields.IntField(null=False)
    nickname = fields.CharField(max_length=128)

    balance = fields.IntField(default=100)

    # 1 - downcountry
    # 2 - hills
    # 3 - caves
    location = fields.IntField(default=1)

    workers = fields.JSONField(default=[])
    # [{
    #     "level": INT,
    #     "exp": INT,
    #     "exp_need": INT,
    #     "multiplier": FLOAT
    # },...]

    mining_timestamp = fields.BigIntField(default=0)
    ores = fields.OneToOneField("models.Ores", "user", null=False)

    @property
    def workers_count(self):
        return len(self.workers)

    @property
    def location_text(self):
        return {
            1: "Downcountry",
            2: "Hills",
            3: "Caves"
        }[self.location]
