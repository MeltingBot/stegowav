from security.encryptors.aes_encryptor import AesEncryptor
from security.enums.encryption_type import EncryptionType
from security.encryptors.fernet_encryptor import FernetEncryptor
from security.encryptors.generic_encryptor import GenericEncryptor
from security.encryptors.none_encryptor import NoneEncryptor
from security.encryptors.rsa_encryptor import RsaEncryptor


class HashingProvider:

    def __init__(self):
        pass

    @staticmethod
    def get_encryptor(hashing_type: HashingProvider) -> GenericEncryptor:
        if not encryption_type or encryption_type == EncryptionType.NONE:
            return NoneEncryptor()

        if encryption_type == EncryptionType.FERNET:
            return FernetEncryptor()

        if encryption_type == EncryptionType.AES:
            return AesEncryptor()

        if encryption_type == EncryptionType.RSA:
            return RsaEncryptor()

        raise ValueError('Could not get Encryptor')
