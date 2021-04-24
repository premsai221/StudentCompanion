from flask_wtf import FlaskForm
from studentcompanion.models import User
from wtforms import StringField, SubmitField, PasswordField, BooleanField, DateTimeField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional



class SignUpForm(FlaskForm):

    name = StringField('Name', validators = [DataRequired(), Length(min=3,max=30)])
    email = StringField('Email', validators = [DataRequired(), Email()])
    number = StringField('Mobile Number',validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

    submit = SubmitField('Submit')

    def validate_number(self,number):
        user = User.query.filter_by(number=number.data).first()
        if user:
            print(user.email)
            raise ValidationError('Number is already in use')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use')



class LoginForm(FlaskForm):

    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    remember = BooleanField('Remember me')

    submit = SubmitField('Login')



class TimeTableForm(FlaskForm):

    m = StringField(validators=[Optional()],default='Monday')
    m1 = StringField(validators=[Optional()],default=' ')
    m2 = StringField(validators=[Optional()],default=' ')
    m3 = StringField(validators=[Optional()],default=' ')
    m4 = StringField(validators=[Optional()],default=' ')
    m5 = StringField(validators=[Optional()],default=' ')
    m6 = StringField(validators=[Optional()],default=' ')
    m7 = StringField(validators=[Optional()],default=' ')
    m8 = StringField(validators=[Optional()],default=' ')
    m9 = StringField(validators=[Optional()],default=' ')
    m10 = StringField(validators=[Optional()],default=' ')
    m11 = StringField(validators=[Optional()],default=' ')
    m12 = StringField(validators=[Optional()],default=' ')
    tu = StringField(validators=[Optional()],default='Tuesday')
    tu1 = StringField(validators=[Optional()],default=' ')
    tu2 = StringField(validators=[Optional()],default=' ')
    tu3 = StringField(validators=[Optional()],default=' ')
    tu4 = StringField(validators=[Optional()],default=' ')
    tu5 = StringField(validators=[Optional()],default=' ')
    tu6 = StringField(validators=[Optional()],default=' ')
    tu7 = StringField(validators=[Optional()],default=' ')
    tu8 = StringField(validators=[Optional()],default=' ')
    tu9 = StringField(validators=[Optional()],default=' ')
    tu10 = StringField(validators=[Optional()],default=' ')
    tu11 = StringField(validators=[Optional()],default=' ')
    tu12 = StringField(validators=[Optional()],default=' ')
    w = StringField(validators=[Optional()],default='Wednesday')
    w1 = StringField(validators=[Optional()],default=' ')
    w2 = StringField(validators=[Optional()],default=' ')
    w3 = StringField(validators=[Optional()],default=' ')
    w4 = StringField(validators=[Optional()],default=' ')
    w5 = StringField(validators=[Optional()],default=' ')
    w6 = StringField(validators=[Optional()],default=' ')
    w7 = StringField(validators=[Optional()],default=' ')
    w8 = StringField(validators=[Optional()],default=' ')
    w9 = StringField(validators=[Optional()],default=' ')
    w10 = StringField(validators=[Optional()],default=' ')
    w11 = StringField(validators=[Optional()],default=' ')
    w12 = StringField(validators=[Optional()],default=' ')
    t = StringField(validators=[Optional()],default='Thursday')
    t1 = StringField(validators=[Optional()],default=' ')
    t2 = StringField(validators=[Optional()],default=' ')
    t3 = StringField(validators=[Optional()],default=' ')
    t4 = StringField(validators=[Optional()],default=' ')
    t5 = StringField(validators=[Optional()],default=' ')
    t6 = StringField(validators=[Optional()],default=' ')
    t7 = StringField(validators=[Optional()],default=' ')
    t8 = StringField(validators=[Optional()],default=' ')
    t9 = StringField(validators=[Optional()],default=' ')
    t10 = StringField(validators=[Optional()],default=' ')
    t11 = StringField(validators=[Optional()],default=' ')
    t12 = StringField(validators=[Optional()],default=' ')
    f = StringField(validators=[Optional()],default='Friday')
    f1 = StringField(validators=[Optional()],default=' ')
    f2 = StringField(validators=[Optional()],default=' ')
    f3 = StringField(validators=[Optional()],default=' ')
    f4 = StringField(validators=[Optional()],default=' ')
    f5 = StringField(validators=[Optional()],default=' ')
    f6 = StringField(validators=[Optional()],default=' ')
    f7 = StringField(validators=[Optional()],default=' ')
    f8 = StringField(validators=[Optional()],default=' ')
    f9 = StringField(validators=[Optional()],default=' ')
    f10 = StringField(validators=[Optional()],default=' ')
    f11 = StringField(validators=[Optional()],default=' ')
    f12 = StringField(validators=[Optional()],default=' ')
    s = StringField(validators=[Optional()],default='Saturday')
    s1 = StringField(validators=[Optional()],default=' ')
    s2 = StringField(validators=[Optional()],default=' ')
    s3 = StringField(validators=[Optional()],default=' ')
    s4 = StringField(validators=[Optional()],default=' ')
    s5 = StringField(validators=[Optional()],default=' ')
    s6 = StringField(validators=[Optional()],default=' ')
    s7 = StringField(validators=[Optional()],default=' ')
    s8 = StringField(validators=[Optional()],default=' ')
    s9 = StringField(validators=[Optional()],default=' ')
    s10 = StringField(validators=[Optional()],default=' ')
    s11 = StringField(validators=[Optional()],default=' ')
    s12 = StringField(validators=[Optional()],default=' ')
    su = StringField(validators=[Optional()],default='Sunday')
    su1 = StringField(validators=[Optional()],default=' ')
    su2 = StringField(validators=[Optional()],default=' ')
    su3 = StringField(validators=[Optional()],default=' ')
    su4 = StringField(validators=[Optional()],default=' ')
    su4 = StringField(validators=[Optional()],default=' ')
    su5 = StringField(validators=[Optional()],default=' ')
    su6 = StringField(validators=[Optional()],default=' ')
    su7 = StringField(validators=[Optional()],default=' ')
    su8 = StringField(validators=[Optional()],default=' ')
    su9 = StringField(validators=[Optional()],default=' ')
    su10 = StringField(validators=[Optional()],default=' ')
    su11 = StringField(validators=[Optional()],default=' ')
    su12 = StringField(validators=[Optional()],default=' ')
    submit = SubmitField('Confirm Update')
