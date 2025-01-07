from PIL import Image
from cloudinary import CloudinaryResource
from cloudinary.uploader import destroy
from django.core.exceptions import ValidationError




class CloudinaryImageValidatorMixin:
    def validate_field(self, field_name):
        field_value = self.cleaned_data.get(field_name)

        # If the field is blank, return None (valid case for optional fields)
        if not field_value:
            return None

        # Validate Cloudinary resource
        if isinstance(field_value, CloudinaryResource):
            return field_value

        # Validate uploaded image
        try:
            img = Image.open(field_value)
            img.verify()  # Ensure the file is a valid image
            return field_value
        except Exception:
            raise ValidationError('Това поле трябва да бъде изображение.')

        return field_value


class DeleteCloudinaryFormValidMixin:
    cloudinary_delete_fields = None  # Accepts a list or tuple of fields

    def form_valid(self, form):
        if not self.cloudinary_delete_fields:
            raise ValueError("The 'cloudinary_delete_fields' attribute must be set as a list or tuple.")

        if not isinstance(self.cloudinary_delete_fields, (list, tuple)):
            raise TypeError("'cloudinary_delete_fields' must be a list or tuple of field names.")

        old_pictures = {
            field: getattr(self.get_object(), field, None)
            for field in self.cloudinary_delete_fields
        }
        response = super().form_valid(form)

        for field, old_picture in old_pictures.items():
            new_picture = getattr(self.object, field, None)

            if old_picture and old_picture != new_picture:
                try:
                    destroy(old_picture.public_id)
                except Exception as e:
                    print(f"Error deleting old file from Cloudinary for field '{field}': {e}")

        return response

# class DeleteCloudinaryFormValidMixin():
#     cloudinary_delete_field = None
#
#     def form_valid(self, form):
#         if not self.cloudinary_delete_field:
#             raise ValueError("The 'cloudinary_delete_field' attribute must be set.")
#
#         old_picture = getattr(self.get_object(), self.cloudinary_delete_field)
#         response = super().form_valid(form)
#         new_picture = getattr(self.object, self.cloudinary_delete_field)
#
#         if old_picture and old_picture != new_picture:
#             try:
#                 destroy(old_picture.public_id)
#             except Exception as e:
#                 print(f"Error deleting old file from Cloudinary: {e}")
#
#         return response

