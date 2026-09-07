# ==========================================
# 1. CAMERA SHUTTER BUTTON
# ==========================================
class CameraMode:
    def press_shutter(self):
        pass

class PhotoMode(CameraMode):
    def press_shutter(self):
        return "📸 Captured a single high-resolution still image."

class VideoMode(CameraMode):
    def press_shutter(self):
        return "🎥 Started recording 4K video footage."

class BurstMode(CameraMode):
    def press_shutter(self):
        return "⚡ Captured 10 rapid-fire photos in 1 second."


# ==========================================
# 2. LUGGAGE CHECK-IN
# ==========================================
class Luggage:
    def process(self):
        pass

class StandardSuitcase(Luggage):
    def process(self):
        return "🧳 Routed automatically to the standard cargo hold conveyor."

class OversizedSurfboard(Luggage):
    def process(self):
        return "🏄 Sent to the special oversized handling belt."

class FragileBox(Luggage):
    def process(self):
        return "🚨 Tagged 'Fragile' and set aside for manual loading."


# ==========================================
# 3. FOOD DELIVERY APP ORDERING
# ==========================================
class Order:
    def place_order(self):
        pass

class RestaurantMeal(Order):
    def place_order(self):
        return "🍔 Kitchen notified. Courier dispatched to pick up hot food."

class GroceryOrder(Order):
    def place_order(self):
        return "🛒 Store picker assigned to gather items before courier arrival."

class DigitalGiftCard(Order):
    def place_order(self):
        return "📧 Voucher code generated and instantly emailed to user."


# ==========================================
# 4. SMART THERMOSTAT ADJUSTMENTS
# ==========================================
class HVACSystem:
    def adjust(self):
        pass

class AirConditioner(HVACSystem):
    def adjust(self):
        return "❄️ Room hot. AC compressor activated to cool down."

class GasFurnace(HVACSystem):
    def adjust(self):
        return "🔥 Room cold. Igniting gas burner to distribute heat."

class EcoFan(HVACSystem):
    def adjust(self):
        return "💨 Temp stable. Running low-energy fan for air circulation."


# ==========================================
# 5. MEDIA PLAYER PLAY BUTTON
# ==========================================
class MediaItem:
    def play(self):
        pass

class AudioTrack(MediaItem):
    def play(self):
        return "🎵 Streaming high-fidelity audio output."

class VideoStream(MediaItem):
    def play(self):
        return "🎬 Rendering video frames and loading external subtitles."

class PodcastEpisode(MediaItem):
    def play(self):
        return "🎙️ Resuming speech audio from your last saved timestamp."


# ==========================================
# 6. SMARTPHONE BIOMETRICS
# ==========================================
class Authenticator:
    def authenticate(self):
        pass

class FingerprintScanner(Authenticator):
    def authenticate(self):
        return "☝️ Hardware sensor read fingerprint matching active profile."

class FaceRecognition(Authenticator):
    def authenticate(self):
        return "👁️ Front camera matched structural 3D face map data."

class PinInterface(Authenticator):
    def authenticate(self):
        return "⌨️ Verified secure 4-to-6 digit numeric passcode."


# ==========================================
# 7. CAR BRAKING SYSTEM
# ==========================================
class BrakeSystem:
    def apply_brake(self):
        pass

class HydraulicBrake(BrakeSystem):
    def apply_brake(self):
        return "🚗 Fluid pressure forced brake pads to pinch the steel discs."

class RegenerativeBrake(BrakeSystem):
    def apply_brake(self):
        return "🔋 Electric motor reversed to slow car down and recharge battery."


# ==========================================
# 8. WEB BROWSER LINKS
# ==========================================
class WebLink:
    def click(self):
        pass

class ExternalLink(WebLink):
    def click(self):
        return "🌐 Redirecting current window to a completely new domain."

class AnchorLink(WebLink):
    def click(self):
        return "⚓ Scrolling smooth-view down to targeted page element ID."

class MailtoLink(WebLink):
    def click(self):
        return "✉️ Launching native system email application with prefilled draft."


# ==========================================
# 9. SOCIAL MEDIA "SHARE" BUTTON
# ==========================================
class Post:
    def share(self):
        pass

class TextPost(Post):
    def share(self):
        return "🔗 Copied plain text link reference to user's device clipboard."

class PhotoPost(Post):
    def share(self):
        return "🖼️ Opening image layout canvas to add filter options before sending."

class VideoPost(Post):
    def share(self):
        return "✂️ Launching video trim interface to select media duration snippet."


# ==========================================
# 10. COOKING KITCHEN APPLIANCE
# ==========================================
class ApplianceMode:
    def cook(self):
        pass

class AirFryMode(ApplianceMode):
    def cook(self):
        return "🍟 Firing rapid high-heat elements with maximum fan circulation."

class PressureCookMode(ApplianceMode):
    def cook(self):
        return "🍲 Sealing steam release valves to build intensive moisture heat."

class SlowCookMode(ApplianceMode):
    def cook(self):
        return "🍲 Supplying long-duration steady low wattage temperature base."


# ==========================================
# DEMONSTRATION OF POLYMORPHISM IN ACTION
# ==========================================
if __name__ == "__main__":
    print("--- TESTING SYSTEM POLYMORPHISM ---\n")

    # 1. Camera Test
    camera_settings = [PhotoMode(), VideoMode(), BurstMode()]
    print("[1. Camera Shutter]")
    for mode in camera_settings:
        print(mode.press_shutter()) # Same method call, different actions

    # 2. Luggage Test
    baggage_conveyor = [StandardSuitcase(), OversizedSurfboard(), FragileBox()]
    print("\n[2. Luggage Check-In]")
    for item in baggage_conveyor:
        print(item.process())

    # 3. Order Test
    checkout_queue = [RestaurantMeal(), GroceryOrder(), DigitalGiftCard()]
    print("\n[3. Food Delivery App]")
    for order in checkout_queue:
        print(order.place_order())

    # 4. HVAC Test
    smart_home_climate = [AirConditioner(), GasFurnace(), EcoFan()]
    print("\n[4. Smart Thermostat]")
    for component in smart_home_climate:
        print(component.adjust())

    # 5. Media Player Test
    playlist = [AudioTrack(), VideoStream(), PodcastEpisode()]
    print("\n[5. Media Player]")
    for track in playlist:
        print(track.play())

    # 6. Biometrics Test
    lock_screen_options = [FingerprintScanner(), FaceRecognition(), PinInterface()]
    print("\n[6. Smartphone Biometrics]")
    for login in lock_screen_options:
        print(login.authenticate())

    # 7. Brake Test
    ev_brakes = [HydraulicBrake(), RegenerativeBrake()]
    print("\n[7. Car Braking System]")
    for brake in ev_brakes:
        print(brake.apply_brake())

    # 8. Web Links Test
    webpage_elements = [ExternalLink(), AnchorLink(), MailtoLink()]
    print("\n[8. Web Browser Links]")
    for link in webpage_elements:
        print(link.click())

    # 9. Social Share Test
    feed_items = [TextPost(), PhotoPost(), VideoPost()]
    print("\n[9. Social Media Share]")
    for post in feed_items:
        print(post.share())

    # 10. Cooking Test
    smart_pot_knob = [AirFryMode(), PressureCookMode(), SlowCookMode()]
    print("\n[10. Cooking Kitchen Appliance]")
    for setting in smart_pot_knob:
        print(setting.cook())

