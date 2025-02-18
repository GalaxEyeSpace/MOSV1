# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adcsattitudeangle177(models.Model):
    roll_angle = models.TextField(db_column='Roll_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch_angle = models.TextField(db_column='Pitch_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yaw_angle = models.TextField(db_column='Yaw_Angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsAttitudeAngle_177'


class Adcsgetangularcovariance193(models.Model):
    x_angular_rate_covar = models.TextField(db_column='X_angular_rate_covar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_angular_rate_covar = models.TextField(db_column='Y_angular_rate_covar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_angular_rate_covar = models.TextField(db_column='Z_angular_rate_covar', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetAngularCovariance_193'


class Adcsgetconsumedcurrentmeasure159(models.Model):
    cur_val_3_3v = models.TextField(db_column='Cur_val_3_3v', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_val_5v = models.TextField(db_column='Cur_val_5v', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vbat = models.TextField(db_column='Vbat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetConsumedCurrentMeasure_159'


class Adcsgetconsumedcurrentmeasure206(models.Model):
    cur_val_3_3v = models.TextField(db_column='Cur_val_3_3v', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_val_5v = models.TextField(db_column='Cur_val_5v', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    vbat = models.TextField(db_column='Vbat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetConsumedCurrentMeasure_206'


class Adcsgetestimatedgyromeasurement189(models.Model):
    est_x_gyro_bias = models.TextField(db_column='Est_x_gyro_bias', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_y_gyro_bias = models.TextField(db_column='Est_y_gyro_bias', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_z_gyro_bias = models.TextField(db_column='Est_z_gyro_bias', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetEstimatedGyroMeasurement_189'


class Adcsgetestimatedinnovation190(models.Model):
    x_innovation_vector = models.TextField(db_column='X_innovation_vector', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_innovation_vector = models.TextField(db_column='Y_innovation_vector', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_innovation_vector = models.TextField(db_column='Z_innovation_vector', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetEstimatedInnovation_190'


class Adcsgetestimationquaternion185(models.Model):
    star_tracker_est_attitude_q1 = models.TextField(db_column='Star_tracker_est_attitude_q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_tracker_est_attitude_q2 = models.TextField(db_column='Star_tracker_est_attitude_q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_tracker_est_attitude_q3 = models.TextField(db_column='Star_tracker_est_attitude_q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetEstimationQuaternion_185'


class Adcsgetestimationrate184(models.Model):
    est_x_angular_rate = models.TextField(db_column='Est_x_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_y_angular_rate = models.TextField(db_column='Est_y_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_z_angular_rate = models.TextField(db_column='Est_z_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetEstimationRate_184'


class Adcsgetfineestimatedangularrates222(models.Model):
    estimated_x_angular_rate = models.TextField(db_column='Estimated_X_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estimated_y_angular_rate = models.TextField(db_column='Estimated_Y_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estimated_z_angular_rate = models.TextField(db_column='Estimated_Z_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetFineEstimatedAngularRates_222'


class Adcsgetmagneticfieldvec133(models.Model):
    x_axis_vec = models.TextField(db_column='X_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_axis_vec = models.TextField(db_column='Y_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_axis_vec = models.TextField(db_column='Z_axis_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetMagneticFieldVec_133'


class Adcsgetmeasurement223(models.Model):
    magnetic_field_x = models.TextField(db_column='Magnetic_Field_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magnetic_field_y = models.TextField(db_column='Magnetic_Field_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magnetic_field_z = models.TextField(db_column='Magnetic_Field_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coarse_sun_x = models.TextField(db_column='Coarse_Sun_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coarse_sun_y = models.TextField(db_column='Coarse_Sun_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    coarse_sun_z = models.TextField(db_column='Coarse_Sun_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sun_x = models.TextField(db_column='Sun_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sun_y = models.TextField(db_column='Sun_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sun_z = models.TextField(db_column='Sun_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_x = models.TextField(db_column='Nadir_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_y = models.TextField(db_column='Nadir_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_z = models.TextField(db_column='Nadir_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_angular_rate = models.TextField(db_column='X_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_angular_rate = models.TextField(db_column='Y_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_angular_rate = models.TextField(db_column='Z_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_wheel_speed = models.TextField(db_column='X_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_wheel_speed = models.TextField(db_column='Y_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_wheel_speed = models.TextField(db_column='Z_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_body_x = models.TextField(db_column='Star_Body_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_body_y = models.TextField(db_column='Star_Body_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_body_z = models.TextField(db_column='Star_Body_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_x = models.TextField(db_column='Star_Orbit_X', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_y = models.TextField(db_column='Star_Orbit_Y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_z = models.TextField(db_column='Star_Orbit_Z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetMeasurement_223'


class Adcsgetnadirvec136(models.Model):
    x_axis_nadir_vec = models.TextField(db_column='X_axis_nadir_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_axis_nadir_vec = models.TextField(db_column='Y_axis_nadir_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_axis_nadir_vec = models.TextField(db_column='Z_axis_nadir_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetNadirVec_136'


class Adcsgetpositioneci181(models.Model):
    x_eci = models.TextField(db_column='X_eci', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_eci = models.TextField(db_column='Y_eci', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_eci = models.TextField(db_column='Z_eci', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetPositionECI_181'


class Adcsgetpositionllh183(models.Model):
    geocentric_long = models.TextField(db_column='Geocentric_long', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    geocentric_lat = models.TextField(db_column='Geocentric_lat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    geocentric_altitude = models.TextField(db_column='Geocentric_altitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetPositionLLH_183'


class Adcsgetpowerandtemperaturemeasurement163(models.Model):
    current_measure = models.TextField(db_column='Current_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensor_current_measure = models.TextField(db_column='Sensor_current_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    reaction_wheel_current_measure = models.TextField(db_column='Reaction_wheel_current_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temperature = models.TextField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_tracker_cur = models.TextField(db_column='Star_Tracker_cur', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magnetometer_cur = models.TextField(db_column='Magnetometer_cur', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_tracker_mcu_temp = models.TextField(db_column='Star_tracker_MCU_temp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetPowerAndTemperatureMeasurement_163'


class Adcsgetquaternioncovariance192(models.Model):
    quaternion_covar_q1 = models.TextField(db_column='Quaternion_covar_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quaternion_covar_q2 = models.TextField(db_column='Quaternion_covar_Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quaternion_covar_q3 = models.TextField(db_column='Quaternion_covar_Q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetQuaternionCovariance_192'


class Adcsgetquaternionerrorvector191(models.Model):
    quaternion_err_q1 = models.TextField(db_column='Quaternion_err_Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quaternion_err_q2 = models.TextField(db_column='Quaternion_err_Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    quaternion_err_q3 = models.TextField(db_column='Quaternion_err_Q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetQuaternionErrorVector_191'


class Adcsgetratesensorvec137(models.Model):
    x_rate = models.TextField(db_column='X_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_rate = models.TextField(db_column='Y_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_rate = models.TextField(db_column='Z_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRateSensorVec_137'


class Adcsgetrawfinesunsensormeasure141(models.Model):
    fss_raw_x_angle = models.TextField(db_column='Fss_raw_x_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_raw_y_angle = models.TextField(db_column='Fss_raw_y_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_capture_status = models.TextField(db_column='Fss_capture_status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_detection_result = models.TextField(db_column='Fss_detection_result', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawFineSunSensorMeasure_141'


class Adcsgetrawgpsmeasurement152(models.Model):
    gps_solution_status = models.TextField(db_column='Gps_solution_status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    num_tracked_gps_sat = models.TextField(db_column='Num_tracked_gps_sat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    num_used_gps_sat = models.TextField(db_column='Num_used_gps_sat', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    xyz_log_counter = models.TextField(db_column='XYZ_log_counter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    range_log_counter = models.TextField(db_column='Range_log_counter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    log_setup_response = models.TextField(db_column='Log_setup_response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gps_ref_week = models.TextField(db_column='Gps_ref_week', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gps_time_ms = models.TextField(db_column='Gps_time_ms', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_ecef = models.TextField(db_column='X_ECEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_velocity = models.TextField(db_column='X_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_ecef = models.TextField(db_column='Y_ECEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_velocity = models.TextField(db_column='Y_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_ecef = models.TextField(db_column='Z_ECEF', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_velocity = models.TextField(db_column='Z_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_pos_standard_dev = models.TextField(db_column='X_pos_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_pos_standard_dev = models.TextField(db_column='Y_pos_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_pos_standard_dev = models.TextField(db_column='Z_pos_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_vel_standard_dev = models.TextField(db_column='X_vel_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_vel_standard_dev = models.TextField(db_column='Y_vel_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_vel_standard_dev = models.TextField(db_column='Z_vel_standard_dev', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawGPSMeasurement_152'


class Adcsgetrawmagnetometermeasure142(models.Model):
    raw_mgmtr_x_msr = models.TextField(db_column='Raw_mgmtr_x_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_mgmtr_y_msr = models.TextField(db_column='Raw_mgmtr_y_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_mgmtr_z_msr = models.TextField(db_column='Raw_mgmtr_z_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawMagnetometerMeasure_142'


class Adcsgetrawmagnetometermeasure155(models.Model):
    raw_mgmtr_x_msr = models.TextField(db_column='Raw_mgmtr_x_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_mgmtr_y_msr = models.TextField(db_column='Raw_mgmtr_y_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_mgmtr_z_msr = models.TextField(db_column='Raw_mgmtr_z_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawMagnetometerMeasure_155'


class Adcsgetrawsensormeasure151(models.Model):
    nadir_sen_raw_x_angle = models.TextField(db_column='Nadir_sen_raw_x_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_sen_raw_y_angle = models.TextField(db_column='Nadir_sen_raw_y_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_sensor_capture_status = models.TextField(db_column='Nadir_sensor_capture_status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_sensor_detection_result = models.TextField(db_column='Nadir_sensor_detection_result', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_raw_x_angle = models.TextField(db_column='Fss_raw_x_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_raw_y_angle = models.TextField(db_column='Fss_raw_y_angle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_capture_status = models.TextField(db_column='Fss_capture_status', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fss_detection_result = models.TextField(db_column='Fss_detection_result', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    css_raw_measurement = models.TextField(db_column='Css_raw_measurement', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_magnetometer_x_measure = models.TextField(db_column='Raw_magnetometer_x_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_magnetometer_y_measure = models.TextField(db_column='Raw_magnetometer_y_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raw_magnetometer_z_measure = models.TextField(db_column='Raw_magnetometer_z_measure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    x_angular_rate = models.TextField(db_column='X_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_angular_rate = models.TextField(db_column='Y_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_angular_rate = models.TextField(db_column='Z_angular_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawSensorMeasure_151'


class Adcsgetrawsensorrates156(models.Model):
    x_raw_sensor_rate = models.TextField(db_column='X_raw_sensor_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_raw_senson_rate = models.TextField(db_column='Y_raw_senson_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_raw_sensor_rate = models.TextField(db_column='Z_raw_sensor_rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawSensorRates_156'


class Adcsgetrawstartrackermeasure153(models.Model):
    num_stars_detected = models.TextField(db_column='Num_stars_detected', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_image_noise = models.TextField(db_column='Star_image_noise', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invalid_star = models.TextField(db_column='Invalid_star', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    num_of_star_identified = models.TextField(db_column='Num_of_star_identified', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_mode = models.TextField(db_column='Identification_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    img_dark_value = models.TextField(db_column='Img_dark_value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    img_capture_success = models.TextField(db_column='Img_capture_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detection_success = models.TextField(db_column='Detection_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_success = models.TextField(db_column='Identification_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attitude_success = models.TextField(db_column='Attitude_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processing_time_error = models.TextField(db_column='Processing_time_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tracking_module_enabled = models.TextField(db_column='Tracking_module_enabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    predictionenabled = models.TextField(db_column='PredictionEnabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comms_error = models.TextField(db_column='Comms_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star1_confidence = models.TextField(db_column='Star1_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star2_confidence = models.TextField(db_column='Star2_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star3_confidence = models.TextField(db_column='Star3_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star1 = models.TextField(db_column='Instr_Mag_star1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star2 = models.TextField(db_column='Instr_Mag_star2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star3 = models.TextField(db_column='Instr_Mag_star3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    capture = models.TextField(db_column='Capture', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detection = models.TextField(db_column='Detection', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification = models.TextField(db_column='Identification', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_x = models.TextField(db_column='Est_rate_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_y = models.TextField(db_column='Est_rate_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_z = models.TextField(db_column='Est_rate_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q1 = models.TextField(db_column='Est_attitude_q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q2 = models.TextField(db_column='Est_attitude_q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q3 = models.TextField(db_column='Est_attitude_q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawStarTrackerMeasure_153'


class Adcsgetrawstartrackermeasure154(models.Model):
    num_stars_detected = models.TextField(db_column='Num_stars_detected', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_image_noise = models.TextField(db_column='Star_image_noise', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    invalid_star = models.TextField(db_column='Invalid_star', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    num_of_star_identified = models.TextField(db_column='Num_of_star_identified', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_mode = models.TextField(db_column='Identification_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    img_dark_value = models.TextField(db_column='Img_dark_value', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    img_capture_success = models.TextField(db_column='Img_capture_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detection_success = models.TextField(db_column='Detection_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_success = models.TextField(db_column='Identification_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attitude_success = models.TextField(db_column='Attitude_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processing_time_error = models.TextField(db_column='Processing_time_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tracking_module_enabled = models.TextField(db_column='Tracking_module_enabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    predictionenabled = models.TextField(db_column='PredictionEnabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comms_error = models.TextField(db_column='Comms_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star1_confidence = models.TextField(db_column='Star1_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star2_confidence = models.TextField(db_column='Star2_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star3_confidence = models.TextField(db_column='Star3_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star1 = models.TextField(db_column='Instr_Mag_star1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star2 = models.TextField(db_column='Instr_Mag_star2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instr_mag_star3 = models.TextField(db_column='Instr_Mag_star3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    capture = models.TextField(db_column='Capture', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detection = models.TextField(db_column='Detection', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification = models.TextField(db_column='Identification', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_x = models.TextField(db_column='Est_rate_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_y = models.TextField(db_column='Est_rate_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_rate_z = models.TextField(db_column='Est_rate_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q1 = models.TextField(db_column='Est_attitude_q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q2 = models.TextField(db_column='Est_attitude_q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    est_attitude_q3 = models.TextField(db_column='Est_attitude_q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRawStarTrackerMeasure_154'


class Adcsgetrwcommandedspeed(models.Model):
    x_wheel_speed = models.TextField(db_column='X_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_wheel_speed = models.TextField(db_column='Y_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_wheel_speed = models.TextField(db_column='Z_wheel_speed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRwCommandedSpeed'


class Adcsgetrwcurrent160(models.Model):
    rw_cur1 = models.TextField(db_column='Rw_cur1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rw_cur2 = models.TextField(db_column='Rw_cur2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rw_cur3 = models.TextField(db_column='Rw_cur3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRwCurrent_160'


class Adcsgetrwmeasuredspeed(models.Model):
    rw1 = models.TextField(db_column='Rw1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rw2 = models.TextField(db_column='Rw2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rw3 = models.TextField(db_column='Rw3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rw4 = models.TextField(db_column='Rw4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetRwMeasuredSpeed'


class Adcsgetsenscurrent158(models.Model):
    nadir_sensor_cur_msr = models.TextField(db_column='Nadir_sensor_cur_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fine_sun_sensor_cur_msr = models.TextField(db_column='Fine_sun_sensor_cur_msr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadir_sram_cur = models.TextField(db_column='Nadir_SRAM_cur', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fine_sun_sensor_sram_cur = models.TextField(db_column='Fine_sun_sensor_SRAM_cur', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetSensCurrent_158'


class Adcsgetsensorratetemp162(models.Model):
    x_sensor_temp_val = models.TextField(db_column='X_sensor_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_sensor_temp_val = models.TextField(db_column='Y_sensor_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_sensor_temp_val = models.TextField(db_column='Z_sensor_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetSensorRateTemp_162'


class Adcsgetstarperformance2244(models.Model):
    img_capture_success = models.TextField(db_column='Img_capture_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    detection_success = models.TextField(db_column='Detection_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    identification_success = models.TextField(db_column='Identification_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    attitude_success = models.TextField(db_column='Attitude_success', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    processing_time_error = models.TextField(db_column='Processing_time_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tracking_module_enabled = models.TextField(db_column='Tracking_module_enabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    predictionenabled = models.TextField(db_column='PredictionEnabled', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    comms_error = models.TextField(db_column='Comms_error', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sample_period = models.TextField(db_column='Sample_period', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star1_confidence = models.TextField(db_column='Star1_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star2_confidence = models.TextField(db_column='Star2_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star3_confidence = models.TextField(db_column='Star3_confidence', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetStarPerformance2_244'


class Adcsgetstartrakerbodyvec138(models.Model):
    star_body_x = models.TextField(db_column='Star_body_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_body_y = models.TextField(db_column='Star_body_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_body_z = models.TextField(db_column='Star_body_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetStarTrakerBodyVec_138'


class Adcsgetstartrakerorbitvec139(models.Model):
    star_id = models.TextField(db_column='Star_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_x = models.TextField(db_column='Star_orbit_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_y = models.TextField(db_column='Star_orbit_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    star_orbit_z = models.TextField(db_column='Star_orbit_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetStarTrakerOrbitVec_139'


class Adcsgetstate129(models.Model):
    adcsrunmode = models.TextField(db_column='AdcsRunMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    altitude = models.TextField(db_column='Altitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    asgp4mode = models.TextField(db_column='Asgp4Mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam1overcurrent3v3 = models.TextField(db_column='Cam1Overcurrent3V3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam1overcurrentsram = models.TextField(db_column='Cam1OvercurrentSram', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam1sensdetecterror = models.TextField(db_column='Cam1SensDetectError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam1sensnotidle = models.TextField(db_column='Cam1SensNotIdle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam2overcurrent3v3 = models.TextField(db_column='Cam2Overcurrent3V3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam2overcurrentsram = models.TextField(db_column='Cam2OvercurrentSram', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam2sensdetecterror = models.TextField(db_column='Cam2SensDetectError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cam2sensnotidle = models.TextField(db_column='Cam2SensNotIdle', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    configinvaliderror = models.TextField(db_column='ConfigInvalidError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    controlmode = models.TextField(db_column='ControlMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    controlmodenotallowed = models.TextField(db_column='ControlModeNotAllowed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    csserror = models.TextField(db_column='CssError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolmotorcommserror = models.TextField(db_column='CubeControlMotorCommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolmotorpower = models.TextField(db_column='CubeControlMotorPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolmotorruntimeerror = models.TextField(db_column='CubeControlMotorRuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolsignalcommserror = models.TextField(db_column='CubeControlSignalCommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolsignalpower = models.TextField(db_column='CubeControlSignalPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubecontrolsignalruntimeerror = models.TextField(db_column='CubeControlSignalRuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense1commserror = models.TextField(db_column='CubeSense1CommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense1power = models.TextField(db_column='CubeSense1Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense1runtimeerror = models.TextField(db_column='CubeSense1RuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense2commserror = models.TextField(db_column='CubeSense2CommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense2power = models.TextField(db_column='CubeSense2Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubesense2runtimeerror = models.TextField(db_column='CubeSense2RuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubestarcommserror = models.TextField(db_column='CubeStarCommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubestarpower = models.TextField(db_column='CubeStarPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubestarruntimeerror = models.TextField(db_column='CubeStarRuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel1commserror = models.TextField(db_column='CubeWheel1CommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel1power = models.TextField(db_column='CubeWheel1Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel1runtimeerror = models.TextField(db_column='CubeWheel1RuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel2commserror = models.TextField(db_column='CubeWheel2CommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel2power = models.TextField(db_column='CubeWheel2Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel2runtimeerror = models.TextField(db_column='CubeWheel2RuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel3commserror = models.TextField(db_column='CubeWheel3CommsError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel3power = models.TextField(db_column='CubeWheel3Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cubewheel3runtimeerror = models.TextField(db_column='CubeWheel3RuntimeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    curmagmode = models.TextField(db_column='CurMagMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estimmode = models.TextField(db_column='EstimMode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    estimatornotallowed = models.TextField(db_column='EstimatorNotAllowed', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gpslnapower = models.TextField(db_column='GpsLnaPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gpsreceiverpower = models.TextField(db_column='GpsReceiverPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    latitude = models.TextField(db_column='Latitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    longitude = models.TextField(db_column='Longitude', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magrangeerror = models.TextField(db_column='MagRangeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magfieldmodelerror = models.TextField(db_column='MagfieldModelError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magnetometererror = models.TextField(db_column='MagnetometerError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    motordriverpower = models.TextField(db_column='MotorDriverPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    nadirsensrangeerror = models.TextField(db_column='NadirSensRangeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    noderecoveryerror = models.TextField(db_column='NodeRecoveryError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    orbitparamsinvaliderror = models.TextField(db_column='OrbitParamsInvalidError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pitch = models.TextField(db_column='Pitch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    posecefx = models.TextField(db_column='PosEcefX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    posecefy = models.TextField(db_column='PosEcefY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    posecefz = models.TextField(db_column='PosEcefZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    positionx = models.TextField(db_column='PositionX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    positiony = models.TextField(db_column='PositionY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    positionz = models.TextField(db_column='PositionZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    q1 = models.TextField(db_column='Q1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    q2 = models.TextField(db_column='Q2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    q3 = models.TextField(db_column='Q3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ratesensrangeerror = models.TextField(db_column='RateSensRangeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ratesensorfailure = models.TextField(db_column='RateSensorFailure', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ratex = models.TextField(db_column='RateX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ratey = models.TextField(db_column='RateY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ratez = models.TextField(db_column='RateZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    roll = models.TextField(db_column='Roll', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    starmatcherror = models.TextField(db_column='StarMatchError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    startrackovercurrent = models.TextField(db_column='StarTrackOvercurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sunabovehorizon = models.TextField(db_column='SunAboveHorizon', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sunsensrangeerror = models.TextField(db_column='SunSensRangeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    velocityx = models.TextField(db_column='VelocityX', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    velocityy = models.TextField(db_column='VelocityY', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    velocityz = models.TextField(db_column='VelocityZ', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wheelspeedrangeerror = models.TextField(db_column='WheelSpeedRangeError', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    yaw = models.TextField(db_column='Yaw', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetState_129'


class Adcsgetsunsensorvec134(models.Model):
    x_axis_sun_vec = models.TextField(db_column='X_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_axis_sun_vec = models.TextField(db_column='Y_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_axis_sun_vec = models.TextField(db_column='Z_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetSunSensorVec_134'


class Adcsgetsunsensorvec135(models.Model):
    x_axis_sun_vec = models.TextField(db_column='X_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_axis_sun_vec = models.TextField(db_column='Y_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_axis_sun_vec = models.TextField(db_column='Z_axis_sun_vec', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetSunSensorVec_135'


class Adcsgettemperature161(models.Model):
    mcu_temp_val = models.TextField(db_column='MCU_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    magnetometer_temp_val = models.TextField(db_column='Magnetometer_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rate_sensor_temp_val = models.TextField(db_column='Rate_sensor_temp_val', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetTemperature_161'


class Adcsgetvelocityeci182(models.Model):
    x_eci_velocity = models.TextField(db_column='X_eci_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    y_eci_velocity = models.TextField(db_column='Y_eci_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    z_eci_velocity = models.TextField(db_column='Z_eci_velocity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsGetVelocityECI_182'


class Adcstle130(models.Model):
    inclination = models.TextField(db_column='Inclination', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eccentricity = models.TextField(db_column='Eccentricity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    raan = models.TextField(db_column='Raan', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    aop = models.TextField(db_column='AoP', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    b_star_drag_term = models.TextField(db_column='B_star_drag_term', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mean_motion = models.TextField(db_column='Mean_motion', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mean_anomaly = models.TextField(db_column='Mean_anomaly', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epoch = models.TextField(db_column='Epoch', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AdcsTle_130'


class Batterrypercantage(models.Model):
    bat_per = models.TextField(db_column='Bat_per', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BatterryPercantage'


class CommandMode(models.Model):
    mode = models.TextField(blank=True, null=True)  # This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Command_Mode'


class CommsTmInfo(models.Model):
    temp_mcu = models.TextField(db_column='Temp_mcu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_fpga = models.TextField(db_column='Temp_fpga', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_xcvr = models.TextField(db_column='Temp_xcvr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv1 = models.TextField(db_column='Temp_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv2 = models.TextField(db_column='Temp_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv3 = models.TextField(db_column='Temp_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vint = models.TextField(blank=True, null=True)  # This field type is a guess.
    volt_vaux = models.TextField(db_column='Volt_vaux', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vbram = models.TextField(db_column='Volt_vbram', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpint = models.TextField(db_column='Volt_vpint', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpaux = models.TextField(db_column='Volt_vpaux', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpdro = models.TextField(db_column='Volt_vpdro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv1 = models.TextField(db_column='Cur_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv2 = models.TextField(db_column='Cur_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv3 = models.TextField(db_column='Cur_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv4 = models.TextField(db_column='Cur_resrv4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv1 = models.TextField(db_column='Power_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv2 = models.TextField(db_column='Power_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv3 = models.TextField(db_column='Power_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv4 = models.TextField(db_column='Power_resrv4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv5 = models.TextField(db_column='Power_resrv5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rsvd = models.TextField(db_column='Rsvd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_tm_info'


class CommsTmPropXlink398(models.Model):
    temp_mcu = models.TextField(db_column='Temp_mcu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_fpga = models.TextField(db_column='Temp_fpga', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_xcvr = models.TextField(db_column='Temp_xcvr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv1 = models.TextField(db_column='Temp_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv2 = models.TextField(db_column='Temp_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_resrv3 = models.TextField(db_column='Temp_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vint = models.TextField(blank=True, null=True)  # This field type is a guess.
    volt_vaux = models.TextField(db_column='Volt_vaux', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vbram = models.TextField(db_column='Volt_vbram', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpint = models.TextField(db_column='Volt_vpint', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpaux = models.TextField(db_column='Volt_vpaux', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vpdro = models.TextField(db_column='Volt_vpdro', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv1 = models.TextField(db_column='Cur_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv2 = models.TextField(db_column='Cur_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv3 = models.TextField(db_column='Cur_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_resrv4 = models.TextField(db_column='Cur_resrv4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv1 = models.TextField(db_column='Power_resrv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv2 = models.TextField(db_column='Power_resrv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv3 = models.TextField(db_column='Power_resrv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv4 = models.TextField(db_column='Power_resrv4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_resrv5 = models.TextField(db_column='Power_resrv5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rsvd = models.TextField(db_column='Rsvd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_tm_prop_xlink_398'


class CommsUhfGetFullCfg814(models.Model):
    sync1 = models.TextField(db_column='Sync1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sync0 = models.TextField(db_column='Sync0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pktlen = models.TextField(db_column='Pktlen', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pktctrl1 = models.TextField(db_column='Pktctrl1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pktctrl0 = models.TextField(db_column='Pktctrl0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addr = models.TextField(db_column='Addr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channr = models.TextField(db_column='Channr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fsctrl1 = models.TextField(db_column='Fsctrl1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fsctrl0 = models.TextField(db_column='Fsctrl0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    freq2 = models.TextField(db_column='Freq2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    freq1 = models.TextField(db_column='Freq1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    freq0 = models.TextField(db_column='Freq0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdmcfg4 = models.TextField(db_column='Mdmcfg4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdmcfg3 = models.TextField(db_column='Mdmcfg3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdmcfg2 = models.TextField(db_column='Mdmcfg2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdmcfg1 = models.TextField(db_column='Mdmcfg1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mdmcfg0 = models.TextField(db_column='Mdmcfg0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    deviatn = models.TextField(db_column='Deviatn', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mcsm2 = models.TextField(db_column='Mcsm2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mcsm1 = models.TextField(db_column='Mcsm1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mcsm0 = models.TextField(db_column='Mcsm0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    foccfg = models.TextField(db_column='Foccfg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bscfg = models.TextField(db_column='Bscfg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agcctrl2 = models.TextField(db_column='Agcctrl2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agcctrl1 = models.TextField(db_column='Agcctrl1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    agcctrl0 = models.TextField(db_column='Agcctrl0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frend1 = models.TextField(db_column='Frend1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frend0 = models.TextField(db_column='Frend0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fscal3 = models.TextField(db_column='Fscal3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fscal2 = models.TextField(db_column='Fscal2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fscal1 = models.TextField(db_column='Fscal1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fscal0 = models.TextField(db_column='Fscal0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    test2 = models.TextField(db_column='Test2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    test1 = models.TextField(db_column='Test1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    test0 = models.TextField(db_column='Test0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table7 = models.TextField(db_column='Pa_table7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table6 = models.TextField(db_column='Pa_table6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table5 = models.TextField(db_column='Pa_table5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table4 = models.TextField(db_column='Pa_table4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table3 = models.TextField(db_column='Pa_table3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table2 = models.TextField(db_column='Pa_table2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table1 = models.TextField(db_column='Pa_table1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pa_table0 = models.TextField(db_column='Pa_table0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iocfg2 = models.TextField(db_column='Iocfg2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iocfg1 = models.TextField(db_column='Iocfg1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iocfg0 = models.TextField(db_column='Iocfg0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_get_full_cfg_814'


class CommsUhfGetTmInfo800(models.Model):
    uptime = models.TextField(db_column='Uptime', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uart0_rx_count = models.TextField(db_column='Uart0_RX_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    uart1_rx_count = models.TextField(db_column='Uart1_RX_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_mode = models.TextField(db_column='Rx_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tx_mode = models.TextField(db_column='Tx_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc1 = models.TextField(db_column='ADC1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc2 = models.TextField(db_column='ADC2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc3 = models.TextField(db_column='ADC3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc4 = models.TextField(db_column='ADC4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc5 = models.TextField(db_column='ADC5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc6 = models.TextField(db_column='ADC6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc7 = models.TextField(db_column='ADC7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc8 = models.TextField(db_column='ADC8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc9 = models.TextField(db_column='ADC9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc10 = models.TextField(db_column='ADC10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_rssi = models.TextField(db_column='Last_rssi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_lqi = models.TextField(db_column='Last_lqi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    last_f_reqest = models.TextField(db_column='Last_F_Reqest', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_sent = models.TextField(db_column='Pkt_sent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cs_count = models.TextField(db_column='CS_Count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_good = models.TextField(db_column='Pkt_good', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_rejected_chksum = models.TextField(db_column='Pkt_Rejected_Chksum', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_rejected_rsvrd = models.TextField(db_column='Pkt_Rejected_Rsvrd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_rejected_othr = models.TextField(db_column='Pkt_Rejected_Othr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rsrvd0 = models.TextField(db_column='Rsrvd0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_get_tm_info_800'


class CommsUhfSetPwrCfg811(models.Model):
    max_dvga_gain = models.TextField(db_column='Max_DVGA_Gain', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_lna_gain = models.TextField(db_column='Max_LNA_Gain', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    lna_sel = models.TextField(db_column='LNA_Sel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    filter_len = models.TextField(db_column='Filter_Len', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_table_sel = models.TextField(db_column='Power_Table_sel', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rf_output_power = models.TextField(db_column='RF_Output_Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_set_pwr_cfg_811'


class CommsUhfSetRxCfg805(models.Model):
    channel_number = models.TextField(db_column='Channel_Number', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modulation_type = models.TextField(db_column='Modulation_Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sync_mode = models.TextField(db_column='Sync_Mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enable_dc_filter = models.TextField(db_column='Enable_DC_filter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fec_enable = models.TextField(db_column='FEC_enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preamble_num = models.TextField(db_column='Preamble_Num', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manchester_enable = models.TextField(db_column='Manchester_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_attenuation = models.TextField(db_column='RX_Attenuation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    base_frequency = models.TextField(db_column='Base_Frequency', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    if_frequnecy = models.TextField(db_column='IF_Frequnecy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel_spacing = models.TextField(db_column='Channel_Spacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frequency_offset = models.TextField(db_column='Frequency_Offset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_rate = models.TextField(db_column='Data_Rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel_bw = models.TextField(db_column='Channel_BW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frequency_deviation = models.TextField(db_column='Frequency_deviation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_sync_time_out = models.TextField(db_column='RX_Sync_Time_Out', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_set_rx_cfg_805'


class CommsUhfSetTxCfg803(models.Model):
    channel_number = models.TextField(db_column='Channel_Number', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    modulation_type = models.TextField(db_column='Modulation_Type', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sync_mode = models.TextField(db_column='Sync_Mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    enable_dc_filter = models.TextField(db_column='Enable_DC_filter', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fec_enable = models.TextField(db_column='FEC_enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    preamble_num = models.TextField(db_column='Preamble_Num', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manchester_enable = models.TextField(db_column='Manchester_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    base_frequency = models.TextField(db_column='Base_Frequency', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    if_frequnecy = models.TextField(db_column='IF_Frequnecy', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel_spacing = models.TextField(db_column='Channel_Spacing', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frequency_offset = models.TextField(db_column='Frequency_Offset', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    data_rate = models.TextField(db_column='Data_Rate', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel_bw = models.TextField(db_column='Channel_BW', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    frequency_deviation = models.TextField(db_column='Frequency_deviation', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_set_tx_cfg_803'


class CommsUhfSetTxPktCfg807(models.Model):
    demod_sync_word = models.TextField(db_column='Demod_sync_word', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_packet_length = models.TextField(db_column='Max_Packet_Length', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    whitening_enable = models.TextField(db_column='Whitening_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    packet_format = models.TextField(db_column='Packet_Format', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    crc_enable = models.TextField(db_column='CRC_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_len_config = models.TextField(db_column='Pkt_Len_Config', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    device_addr = models.TextField(db_column='Device_Addr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_set_tx_pkt_cfg_807'


class CommsUhfSetTxPktCfg809(models.Model):
    demod_sync_word = models.TextField(db_column='Demod_sync_word', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    max_packet_length = models.TextField(db_column='Max_Packet_Length', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    whitening_enable = models.TextField(db_column='Whitening_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    packet_format = models.TextField(db_column='Packet_Format', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    crc_enable = models.TextField(db_column='CRC_Enable', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pkt_len_config = models.TextField(db_column='Pkt_Len_Config', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    device_addr = models.TextField(db_column='Device_Addr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Comms_uhf_set_tx_pkt_cfg_809'


class Controlmode(models.Model):
    mode = models.CharField(max_length=255, blank=True, null=True)
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ControlMode'


class Cumulativepowerdata(models.Model):
    cumulativepower = models.TextField(db_column='cumulativePower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CumulativePowerData'


class DigitalThermostatInfo533(models.Model):
    instance_id = models.TextField(db_column='Instance_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_temp_threshold = models.TextField(db_column='High_temp_threshold', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low_temp_threshold = models.TextField(db_column='Low_temp_threshold', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    po_pin_logic = models.TextField(db_column='Po_pin_logic', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc_resolution = models.TextField(db_column='Adc_resolution', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operating_mode = models.TextField(db_column='Operating_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temperature = models.TextField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Digital_thermostat_info_533'


class Edgetemperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EdgeTemperatureSensor'


class Edgethermometersensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensortime = models.DateTimeField(db_column='SensorTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EdgeThermometerSensor'


class Edgevoltagemonitorsensor(models.Model):
    sensorvoltage = models.TextField(db_column='SensorVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorcurrent = models.TextField(db_column='SensorCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    admepochtime = models.DateTimeField(db_column='AdmEpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EdgeVoltageMonitorSensor'


class EpsGetBtryBrdRdS203(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_volt_count = models.TextField(db_column='Battery_volt_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temp_count = models.TextField(db_column='Battery_temp_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_battery_voltage = models.TextField(db_column='Total_battery_voltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage1 = models.TextField(db_column='Battery_voltage1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage2 = models.TextField(db_column='Battery_voltage2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage3 = models.TextField(db_column='Battery_voltage3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage4 = models.TextField(db_column='Battery_voltage4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage5 = models.TextField(db_column='Battery_voltage5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage6 = models.TextField(db_column='Battery_voltage6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage7 = models.TextField(db_column='Battery_voltage7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_voltage8 = models.TextField(db_column='Battery_voltage8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_current = models.TextField(db_column='Battery_current', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature1 = models.TextField(db_column='Battery_temperature1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature2 = models.TextField(db_column='Battery_temperature2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature3 = models.TextField(db_column='Battery_temperature3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature4 = models.TextField(db_column='Battery_temperature4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature5 = models.TextField(db_column='Battery_temperature5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature6 = models.TextField(db_column='Battery_temperature6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature7 = models.TextField(db_column='Battery_temperature7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temperature8 = models.TextField(db_column='Battery_temperature8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_flag = models.TextField(db_column='Battery_flag', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eps_get_btry_brd_rd_s_203'


class EpsGetBtryBrdStngS203(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    battery_temp_sense_count = models.TextField(db_column='Battery_temp_sense_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    current_limit_charge = models.TextField(db_column='Current_limit_charge', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    current_limit_discharge = models.TextField(db_column='Current_limit_discharge', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temperature_limit_low1 = models.TextField(db_column='Temperature_limit_low1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temperature_limit_high1 = models.TextField(db_column='Temperature_limit_high1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low2 = models.TextField(db_column='Temp_lmt_low2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high2 = models.TextField(db_column='Temp_lmt_high2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low3 = models.TextField(db_column='Temp_lmt_low3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high3 = models.TextField(db_column='Temp_lmt_high3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low4 = models.TextField(db_column='Temp_lmt_low4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high4 = models.TextField(db_column='Temp_lmt_high4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low5 = models.TextField(db_column='Temp_lmt_low5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high5 = models.TextField(db_column='Temp_lmt_high5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low6 = models.TextField(db_column='Temp_lmt_low6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high6 = models.TextField(db_column='Temp_lmt_high6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low7 = models.TextField(db_column='Temp_lmt_low7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high7 = models.TextField(db_column='Temp_lmt_high7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_low8 = models.TextField(db_column='Temp_lmt_low8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lmt_high8 = models.TextField(db_column='Temp_lmt_high8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    heat_mode = models.TextField(db_column='Heat_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    heat_mode_flags = models.TextField(db_column='Heat_mode_flags', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.TimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eps_get_btry_brd_stng_s_203'


class EpsGetConvBrdStngS201(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt_count = models.TextField(db_column='Op_conv_volt_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    resp = models.TextField(db_column='Resp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt1 = models.TextField(db_column='Op_conv_volt1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt2 = models.TextField(db_column='Op_conv_volt2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt3 = models.TextField(db_column='Op_conv_volt3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt4 = models.TextField(db_column='Op_conv_volt4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eps_get_conv_brd_stng_s_201'


class EpsGetOutChnlCurRdS206(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail_count = models.TextField(db_column='Voltage_rail_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail1 = models.TextField(db_column='Voltage_rail1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail2 = models.TextField(db_column='Voltage_rail2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail3 = models.TextField(db_column='Voltage_rail3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail4 = models.TextField(db_column='Voltage_rail4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail5 = models.TextField(db_column='Voltage_rail5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail6 = models.TextField(db_column='Voltage_rail6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail7 = models.TextField(db_column='Voltage_rail7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail8 = models.TextField(db_column='Voltage_rail8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail9 = models.TextField(db_column='Voltage_rail9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail10 = models.TextField(db_column='Voltage_rail10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_rail11 = models.TextField(db_column='Voltage_rail11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eps_get_out_chnl_cur_rd_s_206'


class EpsGetOutChnlStsS206(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel1 = models.TextField(db_column='Channel1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel2 = models.TextField(db_column='Channel2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel3 = models.TextField(db_column='Channel3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel4 = models.TextField(db_column='Channel4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel5 = models.TextField(db_column='Channel5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel6 = models.TextField(db_column='Channel6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel7 = models.TextField(db_column='Channel7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel8 = models.TextField(db_column='Channel8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel9 = models.TextField(db_column='Channel9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel10 = models.TextField(db_column='Channel10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel11 = models.TextField(db_column='Channel11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    channel12 = models.TextField(db_column='Channel12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hrm_rls_left = models.TextField(db_column='Hrm_rls_left', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hrm_rls_right = models.TextField(db_column='Hrm_rls_right', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Eps_get_out_chnl_sts_s_206'


class Estimationmode(models.Model):
    mode = models.CharField(max_length=255, blank=True, null=True)
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EstimationMode'


class Gpstemperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'GPSTemperatureSensor'


class GetProcUtilInfo500(models.Model):
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Get_proc_util_info_500'


class GetSysUptime583(models.Model):
    data = models.TextField(db_column='Data', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Get_sys_uptime_583'


class ImuInfo(models.Model):
    instance_id = models.TextField(db_column='Instance_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accel_x = models.TextField(db_column='Accel_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accel_y = models.TextField(db_column='Accel_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    accel_z = models.TextField(db_column='Accel_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gyro_x = models.TextField(db_column='Gyro_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gyro_y = models.TextField(db_column='Gyro_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    gyro_z = models.TextField(db_column='Gyro_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mag_x = models.TextField(db_column='Mag_x', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mag_y = models.TextField(db_column='Mag_y', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mag_z = models.TextField(db_column='Mag_z', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mag_rhall = models.TextField(db_column='Mag_rhall', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power = models.TextField(db_column='Power', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    odr = models.TextField(db_column='Odr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    range1 = models.TextField(db_column='Range1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    bw = models.TextField(db_column='Bw', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Imu_info'


class Obcpowermonitorsensor(models.Model):
    sensorvbusvoltage = models.TextField(db_column='SensorVBusVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorvshuntvoltage = models.TextField(db_column='SensorVShuntVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorcurrent = models.TextField(db_column='SensorCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorpower = models.TextField(db_column='SensorPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OBCPowerMonitorSensor'


class Obctemperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OBCTemperatureSensor'


class Overview(models.Model):
    frame_sent = models.TextField(blank=True, null=True)  # This field type is a guess.
    frame_received = models.TextField(blank=True, null=True)  # This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Overview'


class Pspowermonitorsensor(models.Model):
    sensorvbusvoltage = models.TextField(db_column='SensorVBusVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorvshuntvoltage = models.TextField(db_column='SensorVShuntVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorcurrent = models.TextField(db_column='SensorCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorpower = models.TextField(db_column='SensorPower', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.IntegerField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSPowerMonitorSensor'


class Pstemperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSTemperatureSensor'


class Psthermometersensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensortime = models.DateTimeField(db_column='SensorTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSThermometerSensor'


class Psvoltagemonitorsensor1(models.Model):
    sensorvoltage = models.TextField(db_column='SensorVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorcurrent = models.TextField(db_column='SensorCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    admepochtime = models.DateTimeField(db_column='AdmEpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSVoltageMonitorSensor1'


class Psvoltagemonitorsensor2(models.Model):
    sensorvoltage = models.TextField(db_column='SensorVoltage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sensorcurrent = models.TextField(db_column='SensorCurrent', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    admepochtime = models.DateTimeField(db_column='AdmEpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PSVoltageMonitorSensor2'


class PsHealthStatusResponseS605(models.Model):
    cpu_usage = models.TextField(db_column='Cpu_usage', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_mem = models.TextField(db_column='Total_mem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    free_mem = models.TextField(db_column='Free_mem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    used_mem = models.TextField(db_column='Used_mem', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_uptime_minutes = models.TextField(db_column='Ps_uptime_minutes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    total_storage_in_mb = models.TextField(db_column='Total_storage_in_MB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    used_storage_in_mb = models.TextField(db_column='Used_storage_in_MB', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time1 = models.TextField(db_column='Ps_utc_current_time1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time2 = models.TextField(db_column='Ps_utc_current_time2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time3 = models.TextField(db_column='Ps_utc_current_time3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time4 = models.TextField(db_column='Ps_utc_current_time4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time5 = models.TextField(db_column='Ps_utc_current_time5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time6 = models.TextField(db_column='Ps_utc_current_time6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time7 = models.TextField(db_column='Ps_utc_current_time7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time8 = models.TextField(db_column='Ps_utc_current_time8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time9 = models.TextField(db_column='Ps_utc_current_time9', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time10 = models.TextField(db_column='Ps_utc_current_time10', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time11 = models.TextField(db_column='Ps_utc_current_time11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time12 = models.TextField(db_column='Ps_utc_current_time12', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time13 = models.TextField(db_column='Ps_utc_current_time13', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time14 = models.TextField(db_column='Ps_utc_current_time14', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time15 = models.TextField(db_column='Ps_utc_current_time15', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time16 = models.TextField(db_column='Ps_utc_current_time16', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time17 = models.TextField(db_column='Ps_utc_current_time17', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time18 = models.TextField(db_column='Ps_utc_current_time18', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time19 = models.TextField(db_column='Ps_utc_current_time19', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ps_utc_current_time20 = models.TextField(db_column='Ps_utc_current_time20', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PS_health_status_response_s_605'


class Payload1Counters(models.Model):
    count1 = models.TextField(db_column='Count1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count2 = models.TextField(db_column='Count2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count3 = models.TextField(db_column='Count3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count4 = models.TextField(db_column='Count4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count5 = models.TextField(db_column='Count5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count6 = models.TextField(db_column='Count6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count7 = models.TextField(db_column='Count7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count8 = models.TextField(db_column='Count8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payload1Counters'


class Payload2Counters(models.Model):
    count1 = models.TextField(db_column='Count1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count2 = models.TextField(db_column='Count2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count3 = models.TextField(db_column='Count3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count4 = models.TextField(db_column='Count4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count5 = models.TextField(db_column='Count5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count6 = models.TextField(db_column='Count6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count7 = models.TextField(db_column='Count7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count8 = models.TextField(db_column='Count8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payload2Counters'


class Payload3Counters(models.Model):
    count1 = models.TextField(db_column='Count1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count2 = models.TextField(db_column='Count2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count3 = models.TextField(db_column='Count3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count4 = models.TextField(db_column='Count4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count5 = models.TextField(db_column='Count5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count6 = models.TextField(db_column='Count6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count7 = models.TextField(db_column='Count7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count8 = models.TextField(db_column='Count8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payload3Counters'


class Payload4Counters(models.Model):
    count1 = models.TextField(db_column='Count1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count2 = models.TextField(db_column='Count2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count3 = models.TextField(db_column='Count3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count4 = models.TextField(db_column='Count4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count5 = models.TextField(db_column='Count5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count6 = models.TextField(db_column='Count6', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count7 = models.TextField(db_column='Count7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    count8 = models.TextField(db_column='Count8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Payload4Counters'


class SCommsRxTm399(models.Model):
    rx_cfg_frames = models.IntegerField(db_column='Rx_cfg_frames', blank=True, null=True)  # Field name made lowercase.
    rx_cfg_detected = models.IntegerField(db_column='Rx_cfg_detected', blank=True, null=True)  # Field name made lowercase.
    rx_cfg_rssi = models.TextField(db_column='Rx_cfg_rssi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_avg_rssi = models.TextField(db_column='Rx_avg_rssi', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_cfg_freqerr = models.TextField(db_column='Rx_cfg_freqerr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_cfg_carrier_lock = models.IntegerField(db_column='Rx_cfg_carrier_lock', blank=True, null=True)  # Field name made lowercase.
    rx_frame_lock = models.TextField(db_column='Rx_frame_lock', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_cfg_symerr = models.TextField(db_column='Rx_cfg_symerr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_cfg_ebn0 = models.TextField(db_column='Rx_cfg_ebn0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    rx_sir_min = models.IntegerField(db_column='Rx_sir_min', blank=True, null=True)  # Field name made lowercase.
    rx_sir_max = models.IntegerField(db_column='Rx_sir_max', blank=True, null=True)  # Field name made lowercase.
    rx_bch_block_cnt = models.IntegerField(db_column='Rx_bch_block_cnt', blank=True, null=True)  # Field name made lowercase.
    rx_bch_err_cnt = models.IntegerField(db_column='Rx_bch_err_cnt', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'S_comms_rx_tm_399'


class SCommsTmProp398(models.Model):
    temp_psu = models.TextField(db_column='Temp_psu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_mcu = models.TextField(db_column='Temp_mcu', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_fpga = models.TextField(db_column='Temp_fpga', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_xcvr = models.TextField(db_column='Temp_xcvr', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_lna = models.TextField(db_column='Temp_lna', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temp_pa = models.TextField(db_column='Temp_pa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_vin = models.TextField(db_column='Volt_vin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_3v3 = models.TextField(db_column='Volt_3v3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_1v8 = models.TextField(db_column='Volt_1v8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_1v0 = models.TextField(db_column='Volt_1v0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    volt_pa = models.TextField(db_column='Volt_pa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_vin = models.TextField(db_column='Cur_vin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_3v3 = models.TextField(db_column='Cur_3v3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_1v8 = models.TextField(db_column='Cur_1v8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_1v0 = models.TextField(db_column='Cur_1v0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cur_pa = models.TextField(db_column='Cur_pa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_vin = models.TextField(db_column='Power_vin', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_3v3 = models.TextField(db_column='Power_3v3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_1v8 = models.TextField(db_column='Power_1v8', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_1v0 = models.TextField(db_column='Power_1v0', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    power_pa = models.TextField(db_column='Power_pa', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'S_comms_tm_prop_398'


class SCommsTxTm400(models.Model):
    tx_cfg_frames = models.TextField(db_column='Tx_cfg_frames', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tx_cfg_pwr_fwd = models.TextField(db_column='Tx_cfg_pwr_fwd', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tx_cfg_pwr_rfl = models.TextField(db_column='Tx_cfg_pwr_rfl', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'S_comms_tx_tm_400'


class Solarpanel1Temperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolarPanel1TemperatureSensor'


class Solarpanel2Temperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolarPanel2TemperatureSensor'


class Solarpanel3Temperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolarPanel3TemperatureSensor'


class Solarpanel4Temperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolarPanel4TemperatureSensor'


class Solarpanel5Temperaturesensor(models.Model):
    tempsensor = models.TextField(db_column='TempSensor', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    epochtime = models.DateTimeField(db_column='EpochTime', blank=True, null=True)  # Field name made lowercase.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolarPanel5TemperatureSensor'


class SysMemStatus501(models.Model):
    iram_heap_mem_total = models.TextField(db_column='Iram_heap_mem_total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iram_heap_mem_used = models.TextField(db_column='Iram_heap_mem_used', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eram_heap_mem_total = models.TextField(db_column='Eram_heap_mem_total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eram_heap_mem_used = models.TextField(db_column='Eram_heap_mem_used', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eflash_qspi_mem_total = models.TextField(db_column='Eflash_qspi_mem_total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eflash_qspi_mem_used = models.TextField(db_column='Eflash_qspi_mem_used', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eflash_fmc_mem_total = models.TextField(db_column='Eflash_fmc_mem_total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eflash_fmc_mem_used = models.TextField(db_column='Eflash_fmc_mem_used', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eram_mem_total = models.TextField(db_column='Eram_mem_total', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    eram_mem_used = models.TextField(db_column='Eram_mem_used', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sys_mem_status_501'


class TctmEpsGetAlertFlag209(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    resp = models.TextField(db_column='Resp', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mode = models.TextField(db_column='Mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    over_curr_ch1_5 = models.TextField(db_column='Over_curr_ch1_5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    over_curr_ch6_11 = models.TextField(db_column='Over_curr_ch6_11', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crnt_btry_chrg = models.TextField(db_column='Ovr_crnt_btry_chrg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crnt_btry_dischrg = models.TextField(db_column='Ovr_crnt_btry_dischrg', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    voltage_blw_10_7 = models.TextField(db_column='Voltage_blw_10_7', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crnt_channel_num = models.TextField(db_column='Ovr_crnt_channel_num', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crbt_log_hours = models.TextField(db_column='Ovr_crbt_log_hours', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crbt_log_minutes = models.TextField(db_column='Ovr_crbt_log_minutes', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    ovr_crbt_log_seconds = models.TextField(db_column='Ovr_crbt_log_seconds', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tctm_eps_get_alert_flag_209'


class TctmEpsGetConvBoardPar201(models.Model):
    eps_sts_var = models.TextField(db_column='Eps_sts_var', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mppt_en_count = models.TextField(db_column='Mppt_en_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_enb_count = models.TextField(db_column='Op_conv_enb_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt_count = models.TextField(db_column='Pv_volt_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur_count = models.TextField(db_column='Pv_cur_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_volt_count = models.TextField(db_column='Op_conv_volt_count', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    response = models.TextField(db_column='Response', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mppt_sts1 = models.TextField(db_column='Mppt_sts1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mppt_sts2 = models.TextField(db_column='Mppt_sts2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mppt_sts3 = models.TextField(db_column='Mppt_sts3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mppt_sts4 = models.TextField(db_column='Mppt_sts4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_enb_sts1 = models.TextField(db_column='Op_conv_enb_sts1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_enb_sts2 = models.TextField(db_column='Op_conv_enb_sts2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_enb_sts3 = models.TextField(db_column='Op_conv_enb_sts3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_conv_enb_sts4 = models.TextField(db_column='Op_conv_enb_sts4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt1 = models.TextField(db_column='Pv_volt1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt2 = models.TextField(db_column='Pv_volt2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt3 = models.TextField(db_column='Pv_volt3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt4 = models.TextField(db_column='Pv_volt4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_volt5 = models.TextField(db_column='Pv_volt5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur1 = models.TextField(db_column='Pv_cur1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur2 = models.TextField(db_column='Pv_cur2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur3 = models.TextField(db_column='Pv_cur3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur4 = models.TextField(db_column='Pv_cur4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pv_cur5 = models.TextField(db_column='Pv_cur5', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_volt_conv1 = models.TextField(db_column='Op_volt_conv1', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_volt_conv2 = models.TextField(db_column='Op_volt_conv2', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_volt_conv3 = models.TextField(db_column='Op_volt_conv3', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    op_volt_conv4 = models.TextField(db_column='Op_volt_conv4', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Tctm_eps_get_conv_board_par_201'


class TempSensInfo525(models.Model):
    instance_id = models.TextField(db_column='Instance_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    device_id = models.TextField(db_column='Device_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    manufacture_id = models.TextField(db_column='Manufacture_id', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    temperature = models.TextField(db_column='Temperature', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    high_temp_threshold = models.TextField(db_column='High_temp_threshold', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    low_temp_threshold = models.TextField(db_column='Low_temp_threshold', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    critical_temp_threshold = models.TextField(db_column='Critical_temp_threshold', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    adc_resolution = models.TextField(db_column='Adc_resolution', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    operating_mode = models.TextField(db_column='Operating_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    polarity = models.TextField(db_column='Polarity', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hysteresis = models.TextField(db_column='Hysteresis', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    window_lock = models.TextField(db_column='Window_lock', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    event_mode = models.TextField(db_column='Event_mode', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    timest = models.DateTimeField(blank=True, null=True)
    synthetictime = models.DateTimeField(db_column='SyntheticTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Temp_sens_info_525'


class AdcsControlMode(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    control_mode = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adcs_control_mode'


class AttErr(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'att_err'


class Attitude(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    roll = models.TextField(blank=True, null=True)  # This field type is a guess.
    pitch = models.TextField(blank=True, null=True)  # This field type is a guess.
    yaw = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'attitude'


class ControlTorque(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'control_torque'


class Omega(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'omega'


class Position(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'position'


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


class Storage(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    instant_data_gen = models.TextField(blank=True, null=True)  # This field type is a guess.
    instant_data_down = models.TextField(blank=True, null=True)  # This field type is a guess.
    ssd_storage = models.TextField(blank=True, null=True)  # This field type is a guess.
    ssd_capacity = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'storage'


class Velocity(models.Model):
    timestep = models.DateTimeField(blank=True, null=True)
    x = models.TextField(blank=True, null=True)  # This field type is a guess.
    y = models.TextField(blank=True, null=True)  # This field type is a guess.
    z = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = True
        db_table = 'Velocity'