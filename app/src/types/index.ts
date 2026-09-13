export * from './content-model';

export interface ProjectConfig {
  project_id: string;
  product_kind: string;
  primary_delivery: string;
  pedagogical_first: boolean;
  language: string;
  age_category: {
    label: string;
    birth_years: number[];
    single_curriculum: boolean;
    individual_adaptation_dimensions: string[];
  };
}

export interface CoachMessageProps {
  childStatement: string;
  coachExplanation: string;
  pedagogicalRationale: string;
  targetBehavior: string;
  ageAppropriateness?: string;
}
