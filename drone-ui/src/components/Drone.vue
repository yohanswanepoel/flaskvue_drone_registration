<template>
  <div class="container">
  <div class="row">
    <div class="col-sm-10">
      <h1>My Drones</h1>
      <hr><br><br>
      <button type="button" class="btn btn-success btn-sm" v-b-modal.drone-modal>Add Drone</button>
      <br><br>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Name</th>
            <th scope="col">Model</th>
            <th scope="col">Weight</th>
            <th scope="col">Serial Number</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(drone,index) in drones" :key="index">
            <td>{{ drone.name }}</td>
            <td>{{ drone.model }}</td>
            <td>{{ drone.weight }}</td>
            <td>{{ drone.serial_number }}</td>
            <td>
              <button type="button" class="btn btn-warning btn-sm">Update</button>
              <button type="button" class="btn btn-danger btn-sm">Delete</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
  <b-modal ref="addDroneModal"
         id="drone-modal"
         title="Add a new drone"
         hide-footer>
  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
  <b-form-group id="form-name-group"
                label="Name:"
                label-for="form-name-input">
      <b-form-input id="form-name-input"
                    type="text"
                    v-model="addDroneForm.name"
                    required
                    placeholder="Enter Name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-model-group"
                  label="Model:"
                  label-for="form-model-input">
        <b-form-input id="form-model-input"
                      type="text"
                      v-model="addDroneForm.model"
                      required
                      placeholder="Enter Model">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-weight-group"
                  label="Weight:"
                  label-for="form-weight-input">
        <b-form-input id="form-weight-input"
                      type="text"
                      v-model="addDroneForm.weight"
                      required
                      placeholder="Enter Weight (grams)">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-serial-group"
                  label="Serial:"
                  label-for="form-serial-input">
        <b-form-input id="form-serial-input"
                      type="text"
                      v-model="addDroneForm.serial_number"
                      required
                      placeholder="Enter Serial Number (grams)">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-date_acquired-group"
                  label="Date Purchased:"
                  label-for="form-date_acquired-input">
        <b-form-input id="form-date_acquired-input"
                      type="date"
                      v-model="addDroneForm.date_acquired"
                      required
                      placeholder="Enter Date Registered">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-new_preowned-group"
                  label="Serial:"
                  label-for="form-new_preowned-input">
        <b-form-input id="form-new_preowned-input"
                      type="text"
                      v-model="addDroneForm.new_preowned"
                      required
                      placeholder="New/Pre-Owned">
        </b-form-input>
      </b-form-group>
    <b-button type="submit" variant="primary">Scan Serial Number</b-button>
    <b-button type="submit" variant="primary">Submit</b-button>
    <b-button type="reset" variant="danger">Reset</b-button>
  </b-form>
</b-modal>
</div>
</template>

<script>
import axios from 'axios';

const url = window.location.hostname;
console.log(url);
const domainURL = url.substring(url.indexOf('.'), url.length);
console.log(domainURL);

export default {
  name: 'Drones',
  data() {
    return {
      drones: [],
      addDroneForm: {
        name: '',
        model: '',
        weight: '',
        serial_number: '',
        date_acquired: '',
        new_preowned: '',
      },
    };
  },
  methods: {
    getDrones() {
      // const path = 'http://python-app-myproject.${domainURL}/books';
      axios.get(`${window.API_URL}/drones`)
        .then((res) => {
          this.drones = res.data.drones;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addDrone(payload) {
      // const path = '/books';
      // const path = 'http://python-app-myproject.${domainURL}/books';
      axios.post(`${window.API_URL}/drones`, payload)
        .then(() => {
          this.getDrones();
        })
        .catch((error) => {
          console.log(error);
          this.getDrones();
        });
    },
    initForm() {
      this.addDroneForm.name = '';
      this.addDroneForm.model = '';
      this.addDroneForm.weight = '';
      this.addDroneForm.serial_number = '';
      this.addDroneForm.date_acquired = '';
      this.addDroneForm.new_preowned = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addDroneModal.hide();
      const payload = {
        name: this.addDroneForm.name,
        model: this.addDroneForm.model,
        weight: this.addDroneForm.weight,
        serial_number: this.addDroneForm.serial_number,
        date_acquired: this.addDroneForm.date_acquired,
        new_preowned: this.addDroneForm.new_preowned,
      };
      this.addDrone(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addDroneModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getDrones();
  },
};

</script>
