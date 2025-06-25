from collections import defaultdict
import matplotlib.pyplot as plt
from math import pi
from imagekitio import ImageKit
import matplotlib
matplotlib.use("Agg")

TESTS_INFO = {
    "gen2_unique_identifier": {"label": "F1", "principle": "F"},
    "gen2_data_identifier_persistence": {"label": "F1", "principle": "F"},
    "gen2_metadata_identifier_persistence": {"label": "F1", "principle": "F"},
    "gen2_grounded_metadata": {"label": "F2", "principle": "F"},
    "gen2_structured_metadata": {"label": "F2", "principle": "F"},
    "gen2_data_identifier_in_metadata": {"label": "F3", "principle": "F"},
    "gen2_metadata_identifier_in_metadata": {"label": "F3", "principle": "F"},
    "gen2_searchable": {"label": "F4", "principle": "F"},
    "gen2_data_protocol": {"label": "A1.1", "principle": "A"},
    "gen2_metadata_protocol": {"label": "A1.1", "principle": "A"},
    "gen2_data_authorization": {"label": "A1.2", "principle": "A"},
    "gen2_metadata_authorization": {"label": "A1.2", "principle": "A"},
    "gen2_metadata_persistence": {"label": "A2", "principle": "A"},
    "gen2_data_kr_language_strong": {"label": "I1", "principle": "I"},
    "gen2_metadata_kr_language_strong": {"label": "I1", "principle": "I"},
    "gen2_data_kr_language_weak": {"label": "I1", "principle": "I"},
    "gen2_metadata_kr_language_weak": {"label": "I1", "principle": "I"},
    "gen2_metadata_uses_fair_vocabularies_strong": {"label": "I2", "principle": "I"},
    "gen2_metadata_uses_fair_vocabularies_weak": {"label": "I2", "principle": "I"},
    "gen2_metadata_contains_outward_links": {"label": "I3", "principle": "I"},
    "gen2_metadata_includes_license_strong": {"label": "R1.1", "principle": "R"},
    "gen2_metadata_includes_license_weak": {"label": "R1.1", "principle": "R"},
}

def aggregate_scores(response):
    scores = defaultdict(list)
    for metric_group in response:
        if not metric_group or not isinstance(metric_group, list):
            continue
        metric = metric_group[0]
        metric_id = metric.get('@id', '')
        score = int(metric["http://semanticscience.org/resource/SIO_000300"][0]["@value"])
        test_name = metric_id.split("/tests/")[-1].split("#")[0]
        if test_name in TESTS_INFO:
            principle = TESTS_INFO[test_name]["principle"]
            scores[principle].append(score)
    final = {}
    for p, values in scores.items():
        final[p] = sum(values) / len(values)
    return final

def generate_radar_chart(principle_scores, output_path):
    categories = list(principle_scores.keys())
    values = list(principle_scores.values())
    values += values[:1]
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    fig = plt.figure()
    ax = plt.subplot(111, polar=True)
    plt.xticks(angles[:-1], categories, color='grey', size=8)
    ax.set_rlabel_position(0)
    plt.yticks([0.25, 0.5, 0.75, 1], ["0.25", "0.5", "0.75", "1"], color="grey", size=7)
    plt.ylim(0, 1)
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    ax.fill(angles, values, 'b', alpha=0.1)
    plt.savefig(output_path)
    plt.close(fig)

def upload_to_imagekit(local_file_path, file_name, public_key, private_key, url_endpoint):
    imagekit = ImageKit(
        public_key=public_key,
        private_key=private_key,
        url_endpoint=url_endpoint
    )
    upload = imagekit.upload(
        file=open(local_file_path, 'rb'),
        file_name=file_name,
    )
    return upload.response_metadata.raw['url']
