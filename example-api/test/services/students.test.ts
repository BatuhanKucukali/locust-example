import assert from 'assert';
import app from '../../src/app';

describe('\'students\' service', () => {
  it('registered the service', () => {
    const service = app.service('students');

    assert.ok(service, 'Registered the service');
  });
});
