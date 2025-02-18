from django.db import models

# Velocity 

class Velocity(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  
    y = models.TextField(blank=True, null=True) 
    z = models.TextField(blank=True, null=True)  

    class Meta:
        managed = True
        db_table = 'velocity'

# Storages 

class Storage(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    instant_data_gen = models.TextField(blank=True, null=True)  # This field type is a guess.
    instant_data_down = models.TextField(blank=True, null=True) 
    ssd_storage = models.TextField(blank=True, null=True)  # This field type is a guess.
    ssd_capacity = models.TextField(blank=True, null=True) 

    class Meta:
        managed = False
        db_table = 'storage'

# Powers

class Power(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    net_power = models.TextField(blank=True, null=True)  # This field type is a guess.
    solar = models.TextField(blank=True, null=True)  # This field type is a guess.
    storage = models.TextField(blank=True, null=True)  # This field type is a guess.
    threshold = models.TextField(blank=True, null=True)  # This field type is a guess.
    power_consumed = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'power'

# Position

class Position(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'position'

# Attitudes

class Adcsattitudeangle177(models.Model):
    roll_angle = models.TextField(db_column='Roll_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch_angle = models.TextField(db_column='Pitch_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yaw_angle = models.TextField(db_column='Yaw_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsAttitudeAngle_177'

class AdcsControlMode(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    control_mode = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adcs_control_mode'

class Adcsgetestimationrate184(models.Model):
    est_x_angular_rate = models.TextField(db_column='Est_x_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_y_angular_rate = models.TextField(db_column='Est_y_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_z_angular_rate = models.TextField(db_column='Est_z_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetEstimationRate_184'

class Adcsgetmagneticfieldvec133(models.Model):
    x_axis_vec = models.TextField(db_column='X_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_axis_vec = models.TextField(db_column='Y_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_axis_vec = models.TextField(db_column='Z_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetMagneticFieldVec_133'

# omegas