/**
 * Content Loader API — ManualFC (TASK-0402)
 * Infață de încărcare și interogare a conținutului canonic pentru aplicația web Astro.
 */

export {
  getProjectConfig,
  getPrimaryNavigation,
  getTaxonomyRegistry,
  getTaxonomyCategories,
  getCategoryById,
  getCategoryBySlug,
  getAllPrinciples,
  getAllExercises,
  getAllProblems,
  getDevelopmentFixtures,
  getCanonicalProductionContent,
  lookupByCanonicalId,
  lookupBySlug,
  getResolvedPrinciple,
  getResolvedExercise,
  getResolvedProblem,
  validateNoDuplicateIds
} from './content-bridge';

export type {
  TaxonomyCategory
} from './content-bridge';
