from deepface import DeepFace
import os

def ID_verification(imge1_path: str, imge2_path: str):
    
    try:
        result = DeepFace.verify(img1_path=imge1_path, img2_path=imge2_path)
        return result

    except Exception as e:
        print(f"Error occurred during ID verification: {e}")
        return None
