class TMDatabaseRouter:
    """
    A database router to direct database operations for telemetry models to the 'tm' database.
    """
    route_app_labels = {'sim'}  # Replace 'sim' with your actual app name

    def db_for_read(self, model, **hints):
        """Direct read operations for sim models to the 'tm' database."""
        if model._meta.app_label in self.route_app_labels:
            return 'tm'
        return None

    def db_for_write(self, model, **hints):
        """Direct write operations for sim models to the 'tm' database."""
        if model._meta.app_label in self.route_app_labels:
            return 'tm'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """Allow relationships between objects in the same database."""
        if obj1._meta.app_label in self.route_app_labels or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that models from 'sim' app only migrate in the 'tm' database."""
        if app_label in self.route_app_labels:
            return db == 'tm'
        return None