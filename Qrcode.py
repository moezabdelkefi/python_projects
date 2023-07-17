import qrcode

def generate_qr_code():
    # Ask the user for the link or text to encode
    data = input("Enter the link in the QR code: ")

    # Generate the QR code
    qr = qrcode.QRCode(version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=1)

    qr.add_data(data)
    qr.make(fit=True)

    # Generate the QR code image with a white background
    qr_image = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code image as a file
    file_name = "qr_code.png"
    qr_image.save(file_name)
    print(f"QR code image saved as '{file_name}'.")

if __name__ == "__main__":
    generate_qr_code()
