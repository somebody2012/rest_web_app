from django.db import models
from django.contrib.auth.hashers import check_password, is_password_usable, make_password

class UserManager(models.Manager):
    def get_by_natural_key(self, username):
        return self.get(**{self.model.USERNAME_FIELD: username})

class CustomUserInfo(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField('password', max_length=128,null=False,blank=False)
    email = models.EmailField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'custom_user_info'

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def is_anonymous(self):
        return False
    @property
    def is_authenticated(self):
        print(self)
        return True

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def __str__(self):
        return self.username



