import { userConstants } from '../_constants';
import { userService } from '../_services';
import { alertActions } from './';
import { history } from '../_helpers';

export const userActions = {
    login,
    logout,
    register,
    getAll,
    delete: _delete
};

function login(username, password) {
    return async dispatch => {
        dispatch(request({ username }));
        try {
            const user = await userService.login(username, password);
            dispatch(success(user));
            history.push('/');
        } catch (error) {
            dispatch(failure(error.toString()));
            debugger;
            dispatch(alertActions.error(error.toString()));
        }

    };

    function request(user) { return { type: userConstants.LOGIN_REQUEST, user } }

    function success(user) { return { type: userConstants.LOGIN_SUCCESS, user } }

    function failure(error) { return { type: userConstants.LOGIN_FAILURE, error } }
}

function logout() {
    userService.logout();
    return { type: userConstants.LOGOUT };
}

function register(user) {
    debugger;
    return async dispatch => {
        dispatch(request(user));
        try {
            const response = await userService.register(user);

            dispatch(success());
            history.push('/login');
            dispatch(alertActions.success('Registration successful'));

        } catch (error) {
            dispatch(failure(error.toString()));
            dispatch(alertActions.error(error.toString()));
        }
    };

    function request(user) { return { type: userConstants.REGISTER_REQUEST, user } }

    function success(user) { return { type: userConstants.REGISTER_SUCCESS, user } }

    function failure(error) { return { type: userConstants.REGISTER_FAILURE, error } }
}

function getAll() {
    return async dispatch => {
        dispatch(request());

        try {
            const users = await userService.getAll();
            dispatch(success(users));

        } catch (error) {
            dispatch(failure(error.toString()))
        }
    };

    function request() { return { type: userConstants.GETALL_REQUEST } }

    function success(users) { return { type: userConstants.GETALL_SUCCESS, users } }

    function failure(error) { return { type: userConstants.GETALL_FAILURE, error } }
}

// prefixed function name with underscore because delete is a reserved word in javascript
function _delete(id) {
    return async dispatch => {
        dispatch(request(id));
        try {
            const user = await userService.delete(id);
            dispatch(success(id));
        } catch (error) {
            dispatch(failure(id, error.toString()))
        }
    };

    function request(id) { return { type: userConstants.DELETE_REQUEST, id } }

    function success(id) { return { type: userConstants.DELETE_SUCCESS, id } }

    function failure(id, error) { return { type: userConstants.DELETE_FAILURE, id, error } }
}