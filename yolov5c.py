import sys
sys.path.append('./yolov5')  # tambahkan path ke repo lokal

from models.common import DetectMultiBackend

model = DetectMultiBackend(weights='models/yolov5s.pt', device='cpu')  # atau 'cuda' jika pakai GPU
