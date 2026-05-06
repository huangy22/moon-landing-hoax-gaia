from gaia.review import ReviewBundle, review_claim, review_strategy

from ..motivation import moon_landing_hoax
from ..conspiracy_claims import (
    obs_flag_waves, obs_no_stars, obs_radiation_belt, obs_shadows,
    obs_footprints, obs_no_crater,
    alt_flag_studio, alt_no_stars_studio, alt_radiation_lethal,
    alt_shadows_studio, alt_footprints_fake, alt_crater_studio,
    _s_anomalies, _s_anomalies_support_real,
)
from ..independent_evidence import (
    obs_retroreflector_us, obs_retroreflector_china,
    alt_retroreflector_unmanned,
    obs_moon_rocks, obs_soviet_samples_match, obs_china_sample,
    alt_rocks_fake,
    obs_lro_images, obs_japan_selene, obs_india_chandrayaan,
    alt_imaging_fake,
    obs_soviet_tracked, obs_soviet_encyclopedia, obs_soviet_luna15,
    alt_soviet_complicit,
    obs_400k_people,
    obs_ouyang_endorsement,
    _s_scale, _s_conspiracy_refutes_hoax, _s_ouyang,
)

REVIEW = ReviewBundle(
    source_id="self_review",
    objects=[
        # ═══════════════════════════════════════════════════════════════
        # Core hypothesis
        # ═══════════════════════════════════════════════════════════════
        review_claim(moon_landing_hoax, prior=0.05,
            judgment="opposing",
            justification=(
                "The hoax hypothesis is rejected by the overwhelming scientific "
                "consensus, multiple independent national space agencies, and "
                "55+ years of corroborating physical evidence. Assign very low prior."
            )),

        # ═══════════════════════════════════════════════════════════════
        # Conspiracy "anomaly" observations — all well-documented
        # ═══════════════════════════════════════════════════════════════
        review_claim(obs_flag_waves, prior=0.95,
            judgment="supporting",
            justification="The flag rippling is clearly visible in archived footage."),
        review_claim(obs_no_stars, prior=0.95,
            judgment="supporting",
            justification="No stars are visible in any Apollo surface photographs."),
        review_claim(obs_radiation_belt, prior=0.99,
            judgment="supporting",
            justification="Apollo trajectories through Van Allen belts are documented fact."),
        review_claim(obs_shadows, prior=0.90,
            judgment="supporting",
            justification="Non-parallel shadows are visible in several Apollo photos."),
        review_claim(obs_footprints, prior=0.95,
            judgment="supporting",
            justification="Sharp bootprints are clearly visible in Apollo surface photos."),
        review_claim(obs_no_crater, prior=0.95,
            judgment="supporting",
            justification="No significant blast crater is visible in photos of LM landing sites."),

        # ═══════════════════════════════════════════════════════════════
        # Hoax "explanations" — all lack explanatory power
        # pi(Alt) = "Can Alt alone explain Obs?" — answer is NO
        # ═══════════════════════════════════════════════════════════════
        review_claim(alt_flag_studio, prior=0.05,
            judgment="opposing",
            justification=(
                "Studio air currents would cause continuous random fluttering, "
                "not the observed pattern of motion only when touched. "
                "The observed motion pattern contradicts the studio hypothesis."
            )),
        review_claim(alt_no_stars_studio, prior=0.05,
            judgment="opposing",
            justification=(
                "The absence of stars is fully explained by camera exposure settings. "
                "A studio backdrop explanation is unnecessary and provides no "
                "additional explanatory power."
            )),
        review_claim(alt_radiation_lethal, prior=0.02,
            judgment="opposing",
            justification=(
                "Dosimetry data from onboard monitors measured ~0.18 rad total. "
                "The claim of lethal radiation ignores transit time and shielding."
            )),
        review_claim(alt_shadows_studio, prior=0.03,
            judgment="opposing",
            justification=(
                "Multiple light sources would produce multiple shadows per object. "
                "No Apollo photo shows multiple shadows. The studio hypothesis "
                "is directly contradicted by the photographic evidence."
            )),
        review_claim(alt_footprints_fake, prior=0.05,
            judgment="opposing",
            justification=(
                "Returned lunar regolith samples confirm angular particle morphology. "
                "The wet sand hypothesis is contradicted by direct sample analysis."
            )),
        review_claim(alt_crater_studio, prior=0.03,
            judgment="opposing",
            justification=(
                "SELENE and Chandrayaan images confirm swept regolith, consistent "
                "with vacuum rocket exhaust. A static prop cannot produce this signature."
            )),

        # ═══════════════════════════════════════════════════════════════
        # Independent evidence observations — all well-documented
        # ═══════════════════════════════════════════════════════════════
        review_claim(obs_retroreflector_us, prior=0.99,
            judgment="supporting",
            justification="Laser ranging experiments have been conducted continuously since 1969."),
        review_claim(obs_retroreflector_china, prior=0.99,
            judgment="supporting",
            justification=(
                "China's Yunnan Observatory (2018) and SYSU TianQin Center (2019) "
                "independently verified all five lunar retroreflectors."
            )),
        review_claim(alt_retroreflector_unmanned, prior=0.15,
            judgment="tentative",
            justification=(
                "Technically possible to place retroreflectors via unmanned probes "
                "(the Soviets did this with Lunokhod). However, this would require an "
                "additional conspiracy: secretly launching unmanned missions while "
                "publicly claiming manned ones. Low but not negligible prior."
            )),
        review_claim(obs_moon_rocks, prior=0.99,
            judgment="supporting",
            justification="381.7 kg of samples analyzed by thousands of scientists over 50+ years."),
        review_claim(obs_soviet_samples_match, prior=0.98,
            judgment="supporting",
            justification="Isotopic match between Apollo and Soviet Luna samples is published science."),
        review_claim(obs_china_sample, prior=0.97,
            judgment="supporting",
            justification="Published in Chinese peer-reviewed journals by CAS scientists."),
        review_claim(alt_rocks_fake, prior=0.01,
            judgment="opposing",
            justification=(
                "Would require thousands of geochemists across dozens of countries "
                "to be either complicit or incompetent for 50+ years. Nano-structures "
                "from micrometeorite impacts cannot be fabricated."
            )),
        review_claim(obs_lro_images, prior=0.98,
            judgment="supporting",
            justification="High-resolution LRO imagery is publicly available and verified."),
        review_claim(obs_japan_selene, prior=0.97,
            judgment="supporting",
            justification="JAXA (Japan) published SELENE results independently."),
        review_claim(obs_india_chandrayaan, prior=0.96,
            judgment="supporting",
            justification="ISRO (India) published Chandrayaan results independently."),
        review_claim(alt_imaging_fake, prior=0.01,
            judgment="opposing",
            justification=(
                "Requires a conspiracy spanning US, Japan, and India — three countries "
                "with independent space programs and no shared motivation to help NASA."
            )),
        review_claim(obs_soviet_tracked, prior=0.95,
            judgment="supporting",
            justification="Soviet deep-space tracking was operational and independently documented."),
        review_claim(obs_soviet_encyclopedia, prior=0.98,
            judgment="supporting",
            justification="The Great Soviet Encyclopedia is a verifiable state publication."),
        review_claim(obs_soviet_luna15, prior=0.97,
            judgment="supporting",
            justification="Luna 15 mission and coordination are documented in both US and Soviet archives."),
        review_claim(alt_soviet_complicit, prior=0.01,
            judgment="opposing",
            justification=(
                "The Soviet Union had every geopolitical motivation to expose a fraud. "
                "Complicity with their primary Cold War rival is implausible."
            )),
        review_claim(obs_400k_people, prior=0.99,
            judgment="supporting",
            justification="Apollo workforce size is documented in NASA records and contractor data."),
        review_claim(obs_ouyang_endorsement, prior=0.98,
            judgment="supporting",
            justification=(
                "Ouyang Ziyuan's statements are publicly documented. He is China's "
                "most authoritative lunar scientist with no allegiance to NASA."
            )),

        # ═══════════════════════════════════════════════════════════════
        # noisy_and strategies — assign conditional probabilities
        # ═══════════════════════════════════════════════════════════════
        review_strategy(_s_anomalies,
            conditional_probability=0.90,
            judgment="formalized",
            justification=(
                "If all six scientific explanations are individually correct, "
                "they jointly explain all anomalies with high probability."
            )),
        review_strategy(_s_anomalies_support_real,
            conditional_probability=0.85,
            judgment="formalized",
            justification=(
                "Explaining away all anomalies removes the hoax hypothesis's "
                "photographic evidence base, but alone doesn't prove the "
                "landings — other evidence lines provide that."
            )),
        review_strategy(_s_scale,
            conditional_probability=0.95,
            judgment="formalized",
            justification="Statistical modeling strongly supports conspiracy implausibility."),
        review_strategy(_s_conspiracy_refutes_hoax,
            conditional_probability=0.90,
            judgment="formalized",
            justification="If large-scale conspiracy is implausible, landings were likely real."),
        review_strategy(_s_ouyang,
            conditional_probability=0.90,
            judgment="formalized",
            justification=(
                "China's independent scientific authority plus independent data "
                "strongly supports landing authenticity."
            )),
    ],
)
