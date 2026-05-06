"""Core hypotheses: Was the Apollo Moon landing real or faked?"""

from gaia.lang import claim, setting, complement

# ── Background ──────────────────────────────────────────────────────────────

space_race = setting(
    "During the Cold War (1957–1972), the United States and the Soviet Union "
    "competed in the 'Space Race.' NASA's Apollo program aimed to land humans "
    "on the Moon, culminating in Apollo 11 on July 20, 1969. Six Apollo missions "
    "(11, 12, 14, 15, 16, 17) successfully landed on the Moon between 1969 and 1972.",
    title="The Space Race and Apollo program",
)

hoax_origin = setting(
    "The Moon-landing conspiracy theory originated with Bill Kaysing's 1976 book "
    "'We Never Went to the Moon: America's Thirty Billion Dollar Swindle.' "
    "Kaysing held a B.A. in English and worked briefly as a technical writer at "
    "Rocketdyne in the 1950s. The theory gained traction through the 2001 Fox TV "
    "special 'Conspiracy Theory: Did We Land on the Moon?'",
    title="Origin of the hoax theory",
)

# ── The two competing hypotheses ────────────────────────────────────────────

moon_landing_real = claim(
    "The Apollo Moon landings (1969–1972) were real: NASA astronauts traveled to "
    "the Moon, walked on its surface, conducted experiments, and returned safely "
    "to Earth. This is supported by the scientific community, multiple independent "
    "space agencies, and 381.7 kg of returned lunar samples.",
    title="Moon landings were real",
)

moon_landing_hoax = claim(
    "The Apollo Moon landings were faked: NASA staged the landings in a film studio "
    "on Earth to win the Space Race, and all photographic/video evidence was "
    "fabricated. The 400,000+ people involved in the Apollo program were either "
    "complicit or deceived.",
    title="Moon landings were a hoax",
)

real_xor_hoax = complement(
    moon_landing_real, moon_landing_hoax,
)
