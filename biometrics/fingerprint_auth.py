import cv2
from skimage.metrics import structural_similarity as ssim

def verify_fingerprint(scanned_path, config):
    ref_path = config.get("biometrics_config", {}).get("reference_fingerprint")
    if not ref_path:
        print("Reference fingerprint path not configured.")
        return False

    ref_img = cv2.imread(ref_path, cv2.IMREAD_GRAYSCALE)
    scan_img = cv2.imread(scanned_path, cv2.IMREAD_GRAYSCALE)

    if ref_img is None or scan_img is None:
        print("Error loading fingerprint images.")
        return False

    # Resize scan to match reference dimensions for comparison
    scan_img = cv2.resize(scan_img, (ref_img.shape[1], ref_img.shape[0]))

    score, _ = ssim(ref_img, scan_img, full=True)
    print(f"Fingerprint Similarity Score: {score:.4f}")

    # Threshold for match confirmation
    if score > 0.75:
        print("Fingerprint authentication successful.")
        return True

    print("Fingerprint authentication failed.")
    return False
