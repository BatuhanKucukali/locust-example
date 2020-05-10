// Initializes the `students` service on path `/students`
import { ServiceAddons } from '@feathersjs/feathers';
import { Application } from '../../declarations';
import { Students } from './students.class';
import hooks from './students.hooks';

// Add this service to the service type index
declare module '../../declarations' {
  interface ServiceTypes {
    'students': Students & ServiceAddons<any>;
  }
}

export default function (app: Application) {
  const options = {
    paginate: app.get('paginate')
  };

  // Initialize our service with any options it requires
  app.use('/students', new Students(options, app));

  // Get our initialized service so that we can register hooks
  const service = app.service('students');

  service.hooks(hooks);
}
