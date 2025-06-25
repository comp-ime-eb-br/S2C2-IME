const tests: Record<string, { label: string, principle: string , type: string}> = {
  gen2_unique_identifier: { label: "F1 gen2_unique_identifier", principle: "F", type: "data" },
  gen2_data_identifier_persistence: { label: "F1 gen2_data_identifier_persistence", principle: "F", type: "data" },
  gen2_metadata_identifier_persistence: { label: "F1 gen2_metadata_identifier_persistence", principle: "F", type: "metadata" },
  gen2_grounded_metadata: { label: "F2 gen2_grounded_metadata", principle: "F", type: "metadata" }, 
  gen2_structured_metadata: { label: "F2 gen2_structured_metadata", principle: "F", type: "metadata" },
  gen2_data_identifier_in_metadata: { label: "F3 gen2_data_identifier_in_metadata", principle: "F", type: "metadata" },
  gen2_metadata_identifier_in_metadata: { label: "F3 gen2_metadata_identifier_in_metadata", principle: "F", type: "metadata" },
  gen2_searchable: { label: "F4 gen2_searchable", principle: "F", type: "metadata"},
  gen2_data_protocol: { label: "A1.1 gen2_data_protocol", principle: "A", type: "data" },
  gen2_metadata_protocol: { label: "A1.1 gen2_metadata_protocol", principle: "A", type: "metadata" },
  gen2_data_authorization: { label: "A1.2 gen2_data_authorization", principle: "A", type: "data" },
  gen2_metadata_authorization: { label: "A1.2 gen2_metadata_authorization", principle: "A", type: "metadata" },
  gen2_metadata_persistence: { label: "A2 gen2_metadata_persistence", principle: "A", type: "metadata" },
  gen2_data_kr_language_strong: { label: "I1 gen2_data_kr_language_strong", principle: "I", type: "data" },
  gen2_metadata_kr_language_strong: { label: "I1 gen2_metadata_kr_language_strong", principle: "I", type: "metadata" },
  gen2_data_kr_language_weak: { label: "I1 gen2_data_kr_language_weak", principle: "I", type: "data" },
  gen2_metadata_kr_language_weak: { label: "I1 gen2_metadata_kr_language_weak", principle: "I", type: "metadata" },
  gen2_metadata_uses_fair_vocabularies_strong: { label: "I2 gen2_metadata_uses_fair_vocabularies_strong", principle: "I", type: "metadata" },
  gen2_metadata_uses_fair_vocabularies_weak: { label: "I2 gen2_metadata_uses_fair_vocabularies_weak", principle: "I", type: "metadata" },
  gen2_metadata_contains_outward_links: { label: "I3 gen2_metadata_contains_outward_links", principle: "I", type: "metadata" },
  gen2_metadata_includes_license_strong: { label: "R1.1 gen2_metadata_includes_license_strong", principle: "R", type: "metadata" },
  gen2_metadata_includes_license_weak: { label: "R1.1 gen2_metadata_includes_license_weak", principle: "R", type: "metadata" }
};

export default tests;