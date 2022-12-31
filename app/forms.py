from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError

class DeleteItemForm(FlaskForm):
    submit = SubmitField(label='Delete Item')

class OrderItemForm(FlaskForm):
    submit = SubmitField(label='Order Item')

class DeclineItemForm(FlaskForm):
    submit = SubmitField(label='Decline Item')

class FulfilItemForm(FlaskForm):
    submit = SubmitField(label='Fulfil Item')

class WLManageForm(FlaskForm):
    deleteSubmit = SubmitField(label='Delete Item')
    orderSubmit = SubmitField(label='Order Item')
    declineSubmit = SubmitField(label='Decline Item')
    fulfilSubmit = SubmitField(label='Fulfil Item')
    cancelSubmit = SubmitField(label='Cancel Item')

class InvModifyForm(FlaskForm):
    checkoutSubmit = SubmitField(label='Checkout Item')
    returnSubmit = SubmitField(label='Return Item')
    updateSubmit = SubmitField(label='Update')
    deleteSubmit = SubmitField(label='Delete Item')